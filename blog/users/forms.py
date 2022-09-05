from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django import forms

from users.models import User_profile

class User_registration_form(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {k:'' for k in fields}

class UserEditForm(UserCreationForm):
    username = forms.CharField(required=False)
    email = forms.EmailField(label="Modificar email", required=False)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput, required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        help_texts = {k:'' for k in fields}
    
class ProfileEditForm(forms.Form):
    description = forms.CharField(required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = User_profile
        fields = ('description', 'image')
        help_texts = {k:'' for k in fields}