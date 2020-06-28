from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.StudentListView.as_view(), name='students'),
    path('student-detail/<int:stu_id>', views.StudentDetailView, name='student-detail'),
    path('student-update/<int:pk>', views.StudentUpdateView.as_view(), name='student-update'),
    path('student-delete/<int:pk>', views.StudentDeleteView.as_view(), name='student-delete'),

    # Profile Related Urls
    path('create_profile/<int:pk>', views.StudentProfileCreate.as_view(), name='create-profile'),
    path('student-profile-list/<int:stu_id>', views.StudentProfileList, name='student-profile-list'),
    path('student-profile/<int:stu_id>', views.StudentProfileDetail, name='student-profile-detail'),
    path('student-profile-update/<int:pk>', views.StudentProfileUpdate.as_view(), name='update-stu-profile'),
    path('student-profile-delete/<int:pk>', views.StudentProfileDelete.as_view(), name='delete-stu-profile'),


    # Student registration
    path('student_registration/', views.student_registration_view, name='student_registration'),

    # MArk TYPE
    path('create_mark_type/', views.MarkTypeCreate.as_view(), name='create_mark_type'),
    path('edit_mark_type/<int:pk>', views.MarkTypeUpdate.as_view(), name='edit_mark_type'),
    path('delete_mark_type/<int:pk>', views.MarkTypeDelete.as_view(), name='delete_mark_type')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
