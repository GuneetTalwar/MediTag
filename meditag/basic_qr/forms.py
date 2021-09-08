from django import forms
from django.forms import ModelForm
#from django.contrib.auth.models import User
from .models import UserProfile

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class addUserInfo(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
