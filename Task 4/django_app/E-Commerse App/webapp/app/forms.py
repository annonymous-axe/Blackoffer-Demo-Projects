from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput

from .models import DiabetesPrediction

# - Regestering/Creating User

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['email', 'username', 'password1', 'password2']


# - Login Form

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# - Create a record

class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = DiabetesPrediction

        fields = ["gender", "age", "hypertension", "heart_disease", "smoking_history", "bmi", "HbA1c_level", 
                  "blood_glucose_level"]