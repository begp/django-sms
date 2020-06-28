from django.urls import path
from .views import AcademyListView, GradeCreateView, TeacherAssignmentCreateView, SubjectCreateView, SectionCreateView, \
    RoomCreateView, GradeUpdateView, SectionUpdateView, SubjectUpdateView, TeacherAssignmentUpdateView, RoomUpdateView, \
    GradeDeleteView, RoomDeleteView, SectionDeleteView, TeacherAssignmentDeleteView, SubjectDeleteView
urlpatterns = [

    path('list', AcademyListView.as_view(), name='academics_list'),
    path('grades/', GradeCreateView.as_view(), name='grade'),
    path('edit-grade/<int:pk>', GradeUpdateView.as_view(), name='edit_grade'),
    path('delete-grade/<int:pk>', GradeDeleteView.as_view(), name='delete_grade'),
    path('room-status/', RoomCreateView.as_view(), name='room'),
    path('edit-room/<int:pk>', RoomUpdateView.as_view(), name='edit_room'),
    path('delete-room/<int:pk>', RoomDeleteView.as_view(), name='delete_room'),
    path('sections/', SectionCreateView.as_view(), name='section'),
    path('edit-section/<int:pk>', SectionUpdateView.as_view(), name='edit_section'),
    path('delete-section/<int:pk>', SectionDeleteView.as_view(), name='delete_section'),
    path('teacher-assignments/', TeacherAssignmentCreateView.as_view(), name='teacher_assign'),
    path('edit-teacher-assign/<int:pk>', TeacherAssignmentUpdateView.as_view(), name='edit_teacher_assign'),
    path('delete-teacher/<int:pk>', TeacherAssignmentDeleteView.as_view(), name='delete_teacher_assign'),
    path('subjects/', SubjectCreateView.as_view(), name='subject'),
    path('edit-subject/<int:pk>', SubjectUpdateView.as_view(), name='edit_subject'),
    path('delete-subject/<int:pk>', SubjectDeleteView.as_view(), name='delete_subject'),
]