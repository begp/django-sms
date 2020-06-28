from django.urls import path
from .views import EmployeeCreateView, EmployeeUpdateView, EmployeeDetailView, EmployeeListView, create_employee_profile, \
    ProfileDeleteView, ProfileUpdateView, EmployeeStatusDetailView

urlpatterns = [

    path('add-employee', EmployeeCreateView.as_view(), name='add_employee'),
    path('edit-employee/<int:pk>', EmployeeUpdateView.as_view(), name='edit_employee'),
    path('<int:pk>/', EmployeeDetailView.as_view(), name='employee_details'),
    path('create-profile/<int:id>/', create_employee_profile, name='create_profile'),
    path('edit-profile/<int:pk>', ProfileUpdateView.as_view(), name='edit_profile'),
    path('delete-profile/<int:pk>', ProfileDeleteView.as_view(), name='delete_profile'),
    path('profile-detail/<int:pk>', EmployeeStatusDetailView.as_view(), name='profile_detail'),
    path('', EmployeeListView.as_view(), name='list_employee'),

]