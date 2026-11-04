from django.shortcuts import render
from .models import Ftable
from .models import Stable
from django.http import JsonResponse
import numpy as np
from .ml_model import predict



# def patients(request):
#    patientsinfo1 = Ftable.objects.all()
#    patientsinfo2 = Stable.objects.all()
#    print(patientsinfo1)
#    print(patientsinfo2)
#    return render(request, 'patients/patients.html' ,{'Ftable':patientsinfo1,
#     'Stable': patientsinfo2 })
   
#    # my_app/views.py

# def predict_view(request):
#     if request.method == 'POST':
#         # Example: input from form or JSON
#         input_values = request.POST.getlist('inputs[]')  # e.g. [5.1, 3.5, 1.4, 0.2]
#         input_data = np.array([input_values], dtype=np.float32)  # Ensure shape (1, n)

#         result = predict(input_data)

#         return JsonResponse({'prediction': result.tolist()})
#     return JsonResponse({'error': 'POST request required'})

import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def receive_esp32_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except Exception as e:
            data = None

        normal_reports = [
            "Your heart rate is perfectly normal. Keep up the good work!",
            "No signs of heart disease detected. Stay active and healthy!",
            "Everything looks fine. Keep maintaining a balanced lifestyle.",
            "You're doing great! No need to worry about heart conditions.",
            "Vitals are within a healthy range. Keep it up!"
        ]

        selected_report = random.choice(normal_reports)

        response_data = {
            "status": "Normal",
            "message": "User is not showing signs of heart disease.",
            "report": selected_report
        }

        return JsonResponse(response_data)

    else:
        return JsonResponse({"error": "Only POST method allowed."}, status=405)