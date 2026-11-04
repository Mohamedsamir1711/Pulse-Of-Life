from rest_framework import serializers
from .models import loginpage
from .forms import SignUpForm

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = loginpage
        fields = ('Email','password')

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUpForm
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')