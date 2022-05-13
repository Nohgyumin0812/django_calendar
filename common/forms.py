from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
  email = forms.EmailField(label = '이메일')
  tel = forms.CharField(label ='전화번호')
  class Meta:
    model = User
    fields = ('username', 'email', 'tel')