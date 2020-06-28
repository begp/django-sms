# from django import forms
#
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from django.contrib.auth.models import Group
from user.models import CustomUser

from .models import EmployeeStatus


class TeacherProfileEditForm(forms.ModelForm):
    role = forms.ModelChoiceField(queryset=Group.objects.all())
    class Meta:
        model = EmployeeStatus
        fields = ('employee_role', 'is_active', 'salary')

    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):

                initial = kwargs.setdefault('initial', {})

                if kwargs['instance'].user_name.groups.all():


                    initial['role'] = kwargs['instance'].user_name.groups.all()[0]
        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self):
        role = self.cleaned_data.pop('role')
        p = super().save()
        p.user_name.groups.set([role])
        return p



class CustomUserCreationForm(UserCreationForm):


    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'password1', 'password2']







