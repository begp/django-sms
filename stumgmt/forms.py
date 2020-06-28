from django.forms import ModelForm
from .models import Student, Father, Mother, Guardian


class StudentRegistrationForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['father_id', 'mother_id', 'guardian_id']


class FatherInfo(ModelForm):
    class Meta:
        model = Father
        fields = '__all__'


class MotherInfo(ModelForm):
    class Meta:
        model = Mother
        fields = '__all__'


class GuardianInfo(ModelForm):
    class Meta:
        model = Guardian
        fields = '__all__'
