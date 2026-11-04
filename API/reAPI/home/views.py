
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import profil
from .models import loginpage
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm, AppointmentForm
from .models import Appointment
from django import forms
from django.http import JsonResponse
from .serializer import LoginSerializer
from .serializer import SignupSerializer
from rest_framework.decorators import api_view


def homepage(request):
   return render(request, 'home/home.html')


DOCTOR_IMAGES = {
    'john_smith': 'image/image9.png',
    'emily_johnson': 'image/image12.png',
    'robert_brown': 'image/13.png',
    'sarah_davis': 'image/image14.png',
    'michael_wilson': 'image/image15.png',
    'jessica_taylor': 'image/image16.png',
}


def appointment(request):
    initial = {}
    if request.user.is_authenticated:
        initial = {
            'full_name': request.user.get_full_name(),
            'email': request.user.email,
        }
    if 'doctor' in request.GET:
        initial['doctor'] = request.GET['doctor']

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appt = form.save(commit=False)
            if request.user.is_authenticated:
                appt.user = request.user
            appt.save()
            request.session['last_appointment_id'] = appt.pk
            return redirect('appointment_success')
    else:
        form = AppointmentForm(initial=initial)

    doctors = []
    for value, label in Appointment.DOCTORS:
        name, _, specialty = label.partition(' — ')
        doctors.append({'value': value, 'name': name, 'specialty': specialty, 'image': DOCTOR_IMAGES.get(value)})

    selected_doctor = form['doctor'].value()
    selected_visit = form['visit_type'].value() or 'in_person'
    return render(request, 'home/appointment.html', {
        'form': form,
        'doctors': doctors,
        'selected_doctor': selected_doctor,
        'selected_visit': selected_visit,
        'visit_types': Appointment.VISIT_TYPES,
    })


def appointment_success(request):
    appt_id = request.session.get('last_appointment_id')
    appt = Appointment.objects.filter(pk=appt_id).first() if appt_id else None
    if appt is None:
        return redirect('appointment')
    return render(request, 'home/appointment_success.html', {
        'appt': appt,
        'doctor_image': DOCTOR_IMAGES.get(appt.doctor),
    })


def navbar(request):
    return render(request, 'home/navbar.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           messages.success(request, ("successfully Login! Welcome"))
           return redirect('home')
        else:
            messages.error(request, ("There was an error login, please try again"))
            return redirect('login')
    else:
        return render(request, 'home/login.html',{})
    

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
          data = form.cleaned_data
          for field_name, value in data.items():
              print(f"{field_name}: {value}")
          user = form.save()
          login(request,user)
          messages.success(request,'You have registered successfully!')
          return redirect('home')
        else:
           messages.error(request, 'Please correct the errors below.')
    return render(request, 'home/signup.html',{'form': form})

def logout_user(request):
    logout(request)     
    messages.success(request,('You have been logged out!'))
    return redirect('home')

@api_view(['GET','POST'])
def login_user_ser(request):
        loginn = loginpage.objects.all()
        serializer = LoginSerializer(loginn, many= True)
        return JsonResponse({'Accounts' : serializer.data})

@api_view(['GET','POST'])
def signup_user_ser(request):
        signup = SignUpForm.cleaned_data
        for field_name, value in signup.items():
            print(f"{field_name}: {value}")
        serializer = SignupSerializer(signup, many= True)
        return JsonResponse({'serializer' : serializer.data})
        