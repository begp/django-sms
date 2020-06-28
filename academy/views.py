from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView

from .forms import GradeForm
from .models import Room, Section, Grade, TeacherAssignment, Subject


class AcademyListView(LoginRequiredMixin, TemplateView):
    template_name = 'academics/list.html'


class GradeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Grade
    form_class = GradeForm
    success_url = reverse_lazy('grade')
    template_name = 'academics/grade.html'

    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False

    def get_context_data(self, **kwargs):
        context = super(GradeCreateView, self).get_context_data(**kwargs)
        context['grades'] = Grade.objects.order_by('grade')

        return context


class GradeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Grade
    template_name = 'academics/grade.html'
    fields = ['grade']
    success_url = reverse_lazy('grade')

    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False

class GradeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Grade
    template_name = 'academics/delete_confirm.html'
    success_url = reverse_lazy('grade')

    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False


class RoomCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Room
    fields = ['block', 'room']
    success_url = reverse_lazy('room')
    template_name = 'academics/room.html'

    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False



    def get_context_data(self, **kwargs):
        context = super(RoomCreateView, self).get_context_data(**kwargs)
        context['rooms'] = Room.objects.order_by('block')
        return context


class RoomUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # new
    model = Room
    template_name = 'academics/room.html'
    fields = ['block', 'room']
    success_url = reverse_lazy('room')

    def test_func(self):
        group = Group.objects.get(name='s')
        return True if group in self.request.user.groups.all() else False


class RoomDeleteView(LoginRequiredMixin, DeleteView):
    model = Room
    template_name = 'academics/delete_confirm.html'
    success_url = reverse_lazy('room')

    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False


class SectionCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Section
    fields = ['grade', 'section', 'room']
    success_url = reverse_lazy('section')
    template_name = 'academics/section.html'
    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False


    def get_context_data(self, **kwargs):
        context = super(SectionCreateView, self).get_context_data(**kwargs)
        context['sections'] = Section.objects.order_by('grade')
        return context


class SectionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # new
    model = Section
    template_name = 'academics/grade.html'
    fields = ['grade', 'section', 'room']
    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False


class SectionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Section
    template_name = 'academics/delete_confirm.html'
    success_url = reverse_lazy('section')

    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False


class TeacherAssignmentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = TeacherAssignment
    fields = ['teacher', 'Section', 'subject']
    success_url = reverse_lazy('teacher_assign')
    template_name = 'academics/teacher_assign_create.html'

    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False


    def get_context_data(self, **kwargs):
        context = super(TeacherAssignmentCreateView, self).get_context_data(**kwargs)
        context['section'] = 'academy'
        context['teachers'] = TeacherAssignment.objects.order_by('teacher')
        # context['t'] = TeacherAssignment.all()
        return context


class TeacherAssignmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # new
    model = TeacherAssignment
    template_name = 'academics/grade.html'
    fields = ['teacher', 'subject', 'Section']
    success_url = reverse_lazy('teacher_assign')

    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False


class TeacherAssignmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TeacherAssignment
    template_name = 'academics/delete_confirm.html'
    success_url = reverse_lazy('teacher_assign')

    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False


class SubjectCreateView(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = Subject
    fields = ['name', 'grade']
    success_url = reverse_lazy('subject')
    template_name = 'academics/subject.html'
    permission_denied_message = 'blah blah blah'

    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False

    def get_context_data(self, **kwargs):
        context = super(SubjectCreateView, self).get_context_data(**kwargs)
        context['subjects'] = Subject.objects.order_by('name')
        return context

    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False


class SubjectUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):  # new
    model = Subject
    template_name = 'academics/subject.html'
    fields = ['name', 'grade']
    success_url = reverse_lazy('section')

    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False


class SubjectDeleteView(LoginRequiredMixin,  UserPassesTestMixin, DeleteView):
    model = Subject
    template_name = 'academics/delete_confirm.html'
    success_url = reverse_lazy('subject')

    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False