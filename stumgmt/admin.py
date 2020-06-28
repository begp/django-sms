from django.contrib import admin
from .models import Student, Father, Mother, Guardian, ActivityMarkType, \
    StudentActivityMark, StudentMark, StudentTotalMark, StudentProfile

# Register your models here.

admin.site.register(Student)
admin.site.register(StudentProfile)
admin.site.register(Father)
admin.site.register(Mother)
admin.site.register(Guardian)
admin.site.register(ActivityMarkType)
admin.site.register(StudentActivityMark)
admin.site.register(StudentMark)
admin.site.register(StudentTotalMark)






