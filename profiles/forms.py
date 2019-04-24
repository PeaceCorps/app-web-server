from django import forms
from django.contrib.auth.models import User
from .models import Pcuser
from django.core.validators import RegexValidator

# Forms convert model fields to HTML fields

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['first_name','last_name','email']


class PcuserForm(forms.ModelForm):

	alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
	first_name = forms.CharField(max_length=30,validators=[alphanumeric])
	last_name = forms.CharField(max_length=30,validators=[alphanumeric])
	photo = forms.FileField()
	email = forms.EmailField()

	class Meta:
		model = Pcuser
		# List of fields to be available in HTML
		fields = ['first_name','last_name','email','phone', 'gender', 'location','photo']


class SignupForm(forms.Form):

    # Extra fields required for signup that are not in PcuserForm
    username = forms.CharField(max_length=30, label='Voornaam')
    email = forms.CharField(max_length=30, label='Achternaam')

    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.save()

    class Meta:
    	model = User
		