from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils import timezone
from .models import Appointment


class AppointmentForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields = ('full_name', 'email', 'phone', 'doctor', 'visit_type', 'date', 'time', 'reason')
		widgets = {
			'full_name': forms.TextInput(attrs={'placeholder': 'e.g. Ahmed Hassan', 'autocomplete': 'name'}),
			'email': forms.EmailInput(attrs={'placeholder': 'you@example.com', 'autocomplete': 'email'}),
			'phone': forms.TextInput(attrs={'placeholder': '+20 100 000 0000', 'autocomplete': 'tel', 'type': 'tel'}),
			'doctor': forms.RadioSelect,
			'visit_type': forms.RadioSelect,
			'date': forms.DateInput(attrs={'type': 'date'}),
			'reason': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Briefly describe your symptoms or the reason for your visit (optional)'}),
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['date'].widget.attrs['min'] = timezone.localdate().isoformat()
		self.fields['time'].choices = [('', 'Select a time')] + list(Appointment.TIME_SLOTS)

	def clean_date(self):
		date = self.cleaned_data['date']
		if date < timezone.localdate():
			raise forms.ValidationError('Please choose today or a future date.')
		return date

	def clean(self):
		cleaned = super().clean()
		doctor, date, time = cleaned.get('doctor'), cleaned.get('date'), cleaned.get('time')
		if doctor and date and time:
			taken = Appointment.objects.filter(doctor=doctor, date=date, time=time).exclude(status='cancelled').exists()
			if taken:
				self.add_error('time', 'This time slot is already booked for the selected doctor. Please pick another time.')
		return cleaned



class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'