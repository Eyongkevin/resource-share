from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from apps.user.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required', label="Email")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class SignInForm(AuthenticationForm):
    class Meta:
        fields = ('username', 'password')
