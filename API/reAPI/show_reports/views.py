from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest 
from rest_framework.decorators import api_view 
from rest_framework.generics import RetrieveUpdateDestroyAPIView
import json
import joblib
from rest_framework import viewsets 
from rest_framework.pagination import PageNumberPagination
from .management.commands.models import Result
from rest_framework.decorators import api_view, authentication_classes, permission_classes 
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .serializers import ResultSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    
class ResultDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ResultSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    
    def get_queryset(self):
        # Make sure you return a valid queryset
        return Result.objects.all()

class ResultPagination(PageNumberPagination):
    page_size = 8


class OpenApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        reports = Result.objects.all()  # استعلام قاعدة البيانات
        serializer = ResultSerializer(reports, many=True, context={'request': request})  # تحويلها إلى JSON
        return Response(serializer.data) 

@csrf_exempt 
def show_reports(request):
    context = {}
    search_pid = request.GET.get('patient_id', '').strip()

    from django.db import connection
    with connection.cursor() as c:
        c.execute("SELECT COUNT(*), COUNT(DISTINCT PatientID), ROUND(AVG(HeartRate), 1), ROUND(AVG(BloodPressure), 1), ROUND(AVG(OxygenSaturation), 1) FROM stable")
        total_rows, total_patients, avg_hr, avg_bp, avg_spo2 = c.fetchone()
        if search_pid.isdigit():
            c.execute("SELECT Age, Sex, ChestPainType, RestingBP, Cholestrol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope, HeartDisease, PatientID, TimeStep, ROUND(HeartRate, 1), ROUND(BloodPressure, 1), ROUND(OxygenSaturation, 1) FROM stable WHERE PatientID = %s ORDER BY TimeStep ASC LIMIT 25", [int(search_pid)])
        else:
            c.execute("SELECT Age, Sex, ChestPainType, RestingBP, Cholestrol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope, HeartDisease, PatientID, TimeStep, ROUND(HeartRate, 1), ROUND(BloodPressure, 1), ROUND(OxygenSaturation, 1) FROM stable LIMIT 25")
        cols = ['age', 'sex', 'chestpaintype', 'restingbp', 'cholestrol', 'fastingbs', 'restingecg', 'maxhr', 'exerciseangina', 'oldpeak', 'st_slope', 'heartdisease', 'patientid', 'timestep', 'heartrate', 'bloodpressure', 'oxygensaturation']
        records = [dict(zip(cols, row)) for row in c.fetchall()]

    context.update({
        'total_rows': total_rows,
        'total_patients': total_patients,
        'avg_hr': avg_hr,
        'avg_bp': avg_bp,
        'avg_spo2': avg_spo2,
        'search_pid': search_pid,
        'records': records,
    })

    if request.method == 'POST':
        try:
            pid = request.POST.get('Patientid', '').strip()
            tstep = request.POST.get('Timestep', '').strip()
            age = request.POST.get('Age', '').strip()
            sex = request.POST.get('Sex', '').strip()
            chest_pain = request.POST.get('ChestPainType', '').strip()
            resting_bp = request.POST.get('RestingBP', '').strip()
            cholesterol = request.POST.get('Cholesterol', '').strip()
            fasting_bs = request.POST.get('FastingBS', '').strip()
            resting_ecg = request.POST.get('RestingECG', '').strip()
            max_hr = request.POST.get('MaxHR', '').strip()
            exercise_angina = request.POST.get('ExerciseAngina', '').strip()
            oldpeak = request.POST.get('Oldpeak', '').strip()
            st_slope = request.POST.get('ST_Slope', '').strip()
            heart_rate = request.POST.get('Heartrate', '').strip()
            blood_pressure = request.POST.get('Bloodpressure', '').strip()
            oxygen_sat = request.POST.get('Oxygensaturation', '').strip()

            matched = None
            if pid.isdigit() and tstep.isdigit():
                matched = Result.objects.filter(patientid=int(pid), timestep=int(tstep)).first()
            if not matched and pid.isdigit():
                matched = Result.objects.filter(patientid=int(pid)).first()
            if not matched and age.isdigit() and resting_bp.isdigit() and cholesterol.isdigit():
                matched = Result.objects.filter(
                    age=int(age), restingbp=int(resting_bp), cholestrol=int(cholesterol)
                ).first()

            if matched:
                hd = matched.heartdisease
                context['checks'] = (
                    f"High Risk — Heart Disease Detected (Database Patient #{matched.patientid}, TimeStep {matched.timestep})"
                    if hd == 1 else
                    f"Normal — No Heart Disease Detected (Database Patient #{matched.patientid}, TimeStep {matched.timestep})"
                )
                context['check_danger'] = (hd == 1)
                context['matched_record'] = matched
            else:
                # Fallback clinical risk check from submitted vitals
                risk_score = 0
                if int(age or 0) > 55: risk_score += 1
                if int(resting_bp or 0) >= 140: risk_score += 1
                if int(cholesterol or 0) >= 240: risk_score += 1
                if int(fasting_bs or 0) == 1: risk_score += 1
                if exercise_angina in ('Y', '1'): risk_score += 2
                if float(oldpeak or 0) >= 1.5: risk_score += 2
                if st_slope in ('Flat', 'Down', '1', '2'): risk_score += 1
                is_high = risk_score >= 3
                context['checks'] = (
                    f"High Risk — Indicators of Heart Disease (Risk Score: {risk_score}/9)"
                    if is_high else
                    f"Normal — Low Heart Disease Risk (Risk Score: {risk_score}/9)"
                )
                context['check_danger'] = is_high

            context['submitted'] = True
            return render(request, 'Show Reports/show_reports.html', context)
        except Exception as e:
            context['error'] = f'Invalid input: {e}'
            return render(request, 'Show Reports/show_reports.html', context, status=400)

    return render(request, 'Show Reports/show_reports.html', context)

@csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def result_list(request, format=None):
    if request.method == 'GET':
        
        results = Result.objects.all()
        serializer = ResultSerializer(results, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        try:
            
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON")
        
        
        serializer = ResultSerializer(data=data)
        if serializer.is_valid():
            
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        else:
            
            return JsonResponse(serializer.errors, status=400)
    
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def result_detail(request, pk, format=None):
    try:
        result = Result.objects.get(pk=pk)
    except Result.DoesNotExist:
        return JsonResponse({'error': 'Result not found'}, status=404)

    if request.method == 'GET':
       
        serializer = ResultSerializer(result)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON")

        serializer = ResultSerializer(result, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        result.delete()
        return JsonResponse({'message': 'Deleted successfully'}, status=204)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
