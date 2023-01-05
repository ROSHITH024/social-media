from django import forms
from api.models import User
from api.models import Post,Comment,UserProfile
from django.contrib.auth.forms import UserCreationForm

class UserRegistration(UserCreationForm):
    password1=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2',]

        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            # 'profile_pic':forms.FileInput(attrs={"class":"form-select"}),
            # 'cover':forms.FileInput(attrs={"class":"form-select"}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=["description","image"]

        widgets={
            "description":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class ProUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["profile_pic","about"]

    widgets={
        'profile_pic':forms.FileInput(attrs={"class":"form-select"}),
        'about':forms.TextInput(attrs={"class":"form-control"}),
    }