from django.urls import path
from .views import EmployeeCreateView, EmployeeUpdateView, EmployeeDetailView, EmployeeListView

urlpatterns = [

    path('add-employee', EmployeeCreateView.as_view(), name='add_employee'),
    path('edit-employee/<int:pk>', EmployeeUpdateView.as_view(), name='edit_employee'),
    path('<int:pk>/', EmployeeDetailView.as_view(), name='employee_details'),
    path('', EmployeeListView.as_view(), name='list_employee'),

]