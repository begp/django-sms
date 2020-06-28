from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import View

from .models import Student, StudentProfile, Father, Mother, Guardian, ActivityMarkType, StudentActivityMark
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .forms import StudentRegistrationForm, FatherInfo, MotherInfo, GuardianInfo


# Create your views here.
from academy.models import Grade, Section


def student(request):
    return render(request, 'base.html')


class StudentListView(generic.ListView):
    model = Student


# registering a student
def student_registration_view(request):
    if request.method == 'POST':
        student_form = StudentRegistrationForm(request.POST or None, request.FILES or None)
        father_form = FatherInfo(request.POST or None, request.FILES or None)
        mother_form = MotherInfo(request.POST or None, request.FILES or None)
        guardian_form = GuardianInfo(request.POST or None, request.FILES or None)

        if father_form.is_valid() & mother_form.is_valid() & guardian_form.is_valid() & student_form.is_valid():
            father_form.clean()
            mother_form.clean()
            guardian_form.clean()
            father_info = father_form.save()
            mother_info = mother_form.save()
            guardian_info = guardian_form.save()

            student_info = student_form.save(False)

            student_info.father_id = father_info
            student_info.mother_id = mother_info
            student_info.guardian_id = guardian_info
            student_info.clean()
            student_info.save()
            return HttpResponseRedirect('/students')
        else:
            return HttpResponseNotFound('<h1>Student form is not valid</h1>', str(student_form.errors))

    else:
        form1 = StudentRegistrationForm()
        form2 = FatherInfo()
        form3 = MotherInfo()
        form4 = GuardianInfo()

        context = {
            'form1': form1,
            'form2': form2,
            'form3': form3,
            'form4': form4
        }
        return render(request, 'stumgmt/student_registration.html', context=context)


# Details of a student, parents and guardian
def StudentDetailView(request, stu_id):
    stu = Student.objects.get(id=stu_id)
    stu_father = Student.objects.select_related('father_id').get(id=stu_id)
    stu_mother = Student.objects.select_related('mother_id').get(id=stu_id)
    stu_guardian = Student.objects.select_related('guardian_id').get(id=stu_id)

    return render(request, 'stumgmt/student_detail.html',
                  {'student_detail': stu, 'father_detail': stu_father, 'mother_detail': stu_mother,
                   'guardian_detail': stu_guardian})


class StudentUpdateView(View):
    form1 = StudentRegistrationForm
    form2 = FatherInfo
    form3 = MotherInfo
    form4 = GuardianInfo
    template_name = 'stumgmt/student_update.html'

    def get(self, request, pk=None):
        stud = get_object_or_404(Student, id=pk)
        stud_form = StudentRegistrationForm(instance=stud)
        father = Student.objects.select_related('father_id').get(id=pk)
        father_form = FatherInfo(prefix=str(father.pk), instance=stud.father_id)
        mother = Student.objects.select_related('mother_id').get(id=pk)
        mother_form = MotherInfo(prefix=str(mother.pk), instance=stud.mother_id)
        guardian = Student.objects.select_related('guardian_id').get(id=pk)
        guardian_form = GuardianInfo(prefix=str(guardian.pk), instance=stud.guardian_id)
        template = 'stumgmt/student_update.html'
        context = {'form1': stud_form, 'form2': father_form, 'form3': mother_form, 'form4': guardian_form}
        return render(request, template, context)

    def post(self, request, pk=None):
        stud = get_object_or_404(Student, id=pk)
        stud_form = StudentRegistrationForm(request.POST, instance=stud)
        father = Student.objects.select_related('father_id').get(id=pk)
        father_form = FatherInfo(request.POST, prefix=str(father.pk), instance=stud.father_id)
        mother = Student.objects.select_related('mother_id').get(id=pk)
        mother_form = MotherInfo(request.POST, prefix=str(mother.pk), instance=stud.mother_id)
        guardian = Student.objects.select_related('guardian_id').get(id=pk)
        guardian_form = GuardianInfo(request.POST, prefix=str(guardian.pk), instance=stud.guardian_id)

        if father_form.is_valid() & mother_form.is_valid() & guardian_form.is_valid() & stud_form.is_valid():
            father_form.clean()
            mother_form.clean()
            guardian_form.clean()
            father_info = father_form.save()
            mother_info = mother_form.save()
            guardian_info = guardian_form.save()

            student_info = stud_form.save(False)

            student_info.father_id = father_info
            student_info.mother_id = mother_info
            student_info.guardian_id = guardian_info
            stud_form.clean()
            stud_form.save()
            return HttpResponseRedirect('/students')
        else:
            return HttpResponseNotFound('<h1>form is not valid</h1>')


class StudentDeleteView(generic.DeleteView):
    model = Student
    template_name = 'stumgmt/student_delete.html'
    success_url = reverse_lazy('students')


######################################################################
# Student Profile CRUD Operations
######################################################################


class StudentProfileCreate(generic.CreateView):
    model = StudentProfile
    fields = '__all__'
    template_name = 'stumgmt/stu_profile_create.html'
    success_url = reverse_lazy('students')


class StudentProfileList(generic.ListView):
    model = StudentProfile


def StudentProfileDetail(request, stu_id):
    stu_profile = StudentProfile.objects.get(stu_id=stu_id)
    stu = StudentProfile.objects.select_related('stu').get(stu_id=stu_id)
    return render(request, 'stumgmt/studentprofile_detail.html',
                  {'stu_profile': stu_profile, 'stu_detail': stu})


class StudentProfileUpdate(generic.UpdateView):
    model = StudentProfile
    fields = '__all__'
    template_name = 'stumgmt/stu_profile_update.html'
    success_url = reverse_lazy('students')


class StudentProfileDelete(generic.DeleteView):
    model = StudentProfile
    template_name = 'stumgmt/stu_profile_delete.html'
    success_url = reverse_lazy('students')


######################################################################
# Student MarksTypes CRUD Operations
######################################################################


class MarkTypeCreate(generic.CreateView):
    model = ActivityMarkType
    fields = '__all__'
    template_name = 'stumgmt/create_mark_type.html'
    success_url = reverse_lazy('create_mark_type')

    def get_context_data(self, **kwargs):
        context = super(MarkTypeCreate, self).get_context_data(**kwargs)
        context['marks'] = ActivityMarkType.objects.order_by('grade')
        context['out_of_60'] = ActivityMarkType.objects.filter
        return context


class MarkTypeUpdate(generic.UpdateView):
    model = ActivityMarkType
    fields = '__all__'
    template_name = 'stumgmt/update_mark_type.html'
    success_url = reverse_lazy('create_mark_type')


class MarkTypeDelete(generic.DeleteView):
    model = ActivityMarkType
    template_name = 'stumgmt/delete_mark_type.html'
    success_url = reverse_lazy('create_mark_type')


######################################################################
# Student  CRUD Operations
######################################################################


class StudentActivityMarkCreate(generic.CreateView):
    model = StudentActivityMark
    fields = '__all__'
    template_name = 'stumgmt/student_activity_mark_create.html'
    success_url = reverse_lazy('create_activity_mark')

    def get_context_data(self, **kwargs):
        context = super(StudentActivityMarkCreate, self).get_context_data(**kwargs)
        context['student'] = StudentActivityMark.objects.order_by('student_profile')
        # context['student_grade'] = Grade.objects.all()
        return context


class StudentActivityMarkUpdate(generic.UpdateView):
    model = StudentActivityMark
    fields = '__all__'
    template_name = 'stumgmt/student_activity_mark_create.html'
    success_url = reverse_lazy('create_activity_mark')


class StudentActivityMarkDelete(generic.DeleteView):
    model = StudentActivityMark
    template_name = 'stumgmt/student_activity_mark_delete.html'
    success_url = reverse_lazy('create_activity_mark')
