from django import forms
from django.contrib.auth import get_user_model

from .models import Grade


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ('grade',)
