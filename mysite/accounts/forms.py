from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class Signup(UserCreationForm):
    profile_image = forms.ImageField(required=False,widget=forms.FileInput(attrs={'class':'form-control'}))
    address=forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class':'form-control'}  ))
    line1=forms.CharField(max_length=300,required=True, widget=forms.TextInput(attrs={'class':'form-control'}  ))
    city=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}  ))
    state=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}  ))
    pincode=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',"type":'number'}))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password from numbers and letters of the Latin alphabet'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirm'}))
    
    class Meta:
        model=User
        fields=['username','email','first_name', 'last_name','password1','password2','profile_image','address','line1','city','state','pincode']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'hi@gmail.com'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'name'}),
        }