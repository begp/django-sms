from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView

from .forms import GradeForm
from .models import Room, Section, Grade, TeacherAssignment, Subject


class AcademyListView(TemplateView):
    template_name = 'academics/list.html'


class GradeCreateView(CreateView):
    model = Grade
    form_class = GradeForm
    success_url = reverse_lazy('grade')
    template_name = 'academics/grade.html'

    def get_context_data(self, **kwargs):
        context = super(GradeCreateView, self).get_context_data(**kwargs)
        context['grades'] = Grade.objects.order_by('grade')

        return context


class GradeUpdateView(UpdateView):
    model = Grade
    template_name = 'academics/grade.html'
    fields = ['grade']
    success_url = reverse_lazy('grade')


class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'academics/delete_confirm.html'
    success_url = reverse_lazy('grade')


class RoomCreateView(CreateView):
    model = Room
    fields = ['block', 'room']
    success_url = reverse_lazy('room')
    template_name = 'academics/room.html'

    def get_context_data(self, **kwargs):
        context = super(RoomCreateView, self).get_context_data(**kwargs)
        context['rooms'] = Room.objects.order_by('block')
        return context


class RoomUpdateView(UpdateView):  # new
    model = Room
    template_name = 'academics/room.html'
    fields = ['block', 'room']
    success_url = reverse_lazy('room')


class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'academics/delete_confirm.html'
    success_url = reverse_lazy('room')


class SectionCreateView(CreateView):
    model = Section
    fields = ['grade', 'section', 'room']
    success_url = reverse_lazy('section')
    template_name = 'academics/section.html'

    def get_context_data(self, **kwargs):
        context = super(SectionCreateView, self).get_context_data(**kwargs)
        context['sections'] = Section.objects.order_by('grade')
        return context


class SectionUpdateView(UpdateView):  # new
    model = Section
    template_name = 'academics/grade.html'
    fields = ['grade', 'section', 'room']


class SectionDeleteView(DeleteView):
    model = Section
    template_name = 'academics/delete_confirm.html'
    success_url = reverse_lazy('section')


class TeacherAssignmentCreateView(CreateView):
    model = TeacherAssignment
    fields = ['teacher', 'Section', 'subject']
    success_url = reverse_lazy('teacher_assign')
    template_name = 'academics/teacher_assign_create.html'

    def get_context_data(self, **kwargs):
        context = super(TeacherAssignmentCreateView, self).get_context_data(**kwargs)
        context['section'] = 'academy'
        context['teachers'] = TeacherAssignment.objects.order_by('teacher')
        # context['t'] = TeacherAssignment.all()
        return context


class TeacherAssignmentUpdateView(UpdateView):  # new
    model = TeacherAssignment
    template_name = 'academics/grade.html'
    fields = ['teacher', 'subject', 'Section']
    success_url = reverse_lazy('teacher_assign')


class TeacherAssignmentDeleteView(DeleteView):
    model = TeacherAssignment
    template_name = 'academics/delete_confirm.html'
    success_url = reverse_lazy('teacher_assign')


class SubjectCreateView(CreateView):
    model = Subject
    fields = ['name', 'grade']
    success_url = reverse_lazy('subject')
    template_name = 'academics/subject.html'

    def get_context_data(self, **kwargs):
        context = super(SubjectCreateView, self).get_context_data(**kwargs)
        context['subjects'] = Subject.objects.order_by('name')
        return context


class SubjectUpdateView(UpdateView):  # new
    model = Subject
    template_name = 'academics/subject.html'
    fields = ['name', 'grade']
    success_url = reverse_lazy('section')


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'academics/delete_confirm.html'
    success_url = reverse_lazy('subject')

