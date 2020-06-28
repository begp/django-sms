from django.contrib import admin
from .models import EmployeeInfo, EmployeeStatus


admin.site.register(EmployeeInfo)
admin.site.register(EmployeeStatus)