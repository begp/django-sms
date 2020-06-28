from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.forms import SetPasswordForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
    ))


class UserPassChangeForm(forms.Form):



    error_messages = {
                   'password_mismatch': ('The two password fields didn’t match.'),
               }
    new_password1 = forms.CharField(
                   label=("New password"),
                   widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
                   strip=False,
                   help_text=password_validation.password_validators_help_text_html(),
               )
    new_password2 = forms.CharField(
                   label=("New password confirmation"),
                   strip=False,
                   widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
               )
    field_order = ('password1', 'password2')

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password2, None)
        return password2