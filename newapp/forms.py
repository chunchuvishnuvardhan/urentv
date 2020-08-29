from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import contact,Feedback,Product
class Createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"

class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields=['name','contact','email','desc']
class feedbackform(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['name','email','feedback']
