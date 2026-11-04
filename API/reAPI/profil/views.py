from django.shortcuts import render


# Create your views here.

def profile(request):

    # datainfo =  patientinfo(request.POST)
    # if datainfo.is_valid():
    #     datainfo.save()
       
    return render(request,'profil/Profile.html')