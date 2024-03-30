from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class TortasForm(forms.ModelForm):
     class Meta:

        model = Tortas
        fields = '__all__'

class CateringForm(forms.ModelForm):
     class Meta:

        model = Catering
        fields = '__all__'

class PasteleriaForm(forms.ModelForm):
     class Meta:

        model = Pasteleria
        fields = '__all__'
    
   
class CapacitacionesForm(forms.ModelForm):
     class Meta:

        model = Capacitaciones
        fields = '__all__'


#_____________Registro Form con validación de email____________
        
class RegistroForm(UserCreationForm): 
    email = forms.EmailField(required=True)   
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma Contraseña", widget=forms.PasswordInput)


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está en uso. Por favor, elige otro.')
        return email 

class UserEditForm(UserChangeForm): 
    email = forms.EmailField(required=True)   
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)
   
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]    

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)