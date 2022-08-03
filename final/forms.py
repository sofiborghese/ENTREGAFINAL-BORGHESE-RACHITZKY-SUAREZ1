from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm (UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget= forms.PasswordInput)

class Meta:
    model = User
    fields = ["username", "email", "password1", "password2"]

    #Saca los mensajes de ayuda
    help_texts = {k:"" for k in fields}

# class UserRegisterForm(UserCreationForm):
#     email= forms.EmailField()
#     password1: forms.CharField(label='Contraseña',widget=forms.PasswordInput)
#     password2: forms.CharField(label='Repetir la Contraseña',widget=forms.PasswordInput)
    
#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2']
#         help_texts = {k:"" for k in fields}


class UserEditForm(forms.Form):
    
    email = forms.EmailField(label='Modificar e-mail', required=False)
    #first_name = forms.CharField(label='Nombre', max_length=30, required=False)
    #last_name = forms.CharField(label='Apellido', max_length=30, required=False)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Repetir Password', widget=forms.PasswordInput, required=False)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email','password1','password2']
        help_texts = {k:"" for k in fields}