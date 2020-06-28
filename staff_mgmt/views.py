from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .forms import CustomUserCreationForm, TeacherProfileEditForm
from .models import EmployeeInfo, EmployeeStatus


class EmployeeCreateView(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = EmployeeInfo
    fields = '__all__'
    success_url = reverse_lazy('list_employee')
    template_name = 'staff_mgmt/add_employee.html'

    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False

    # def get_context_data(self, **kwargs):
    #     context = super(EmployeeCreateView, self).get_context_data(**kwargs)
    #     context['employees'] = EmployeeInfo.objects.order_by('name')
    #     return context


class EmployeeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # new
    model = EmployeeInfo
    template_name = 'staff_mgmt/add_employee.html'
    fields = '__all__'
    # success_url = reverse_lazy('list_employee')
    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False


class EmployeeListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = EmployeeInfo
    template_name = 'staff_mgmt/list_employee.html'
    paginate_by = 20
    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False

class EmployeeDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = EmployeeInfo
    template_name = 'staff_mgmt/employee_detail.html'
    # def get_context_data(self, **kwargs):
    #     context = super(EmployeeDetailView, self).get_context_data(**kwargs)
    #     context['profile'] = self.model.objects.select_related('profile').get(id=kwargs['object'].id)
    #     return context
    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False

class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # new
    model = EmployeeStatus
    template_name = 'staff_mgmt/profile_delete.html'
    success_url = reverse_lazy('list_employee')
    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False

class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # new
    model = EmployeeStatus
    form_class = TeacherProfileEditForm
    template_name = 'staff_mgmt/add_employee.html'
    # fields = '__all__'
    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False

class EmployeeStatusDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = EmployeeStatus
    template_name = 'staff_mgmt/employee_status_detail.html'
    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False


def user_access_check(user):
    group = Group.objects.get(name='director')
    return True if group in user.groups.all() else False



@login_required
@user_passes_test(user_access_check, redirect_field_name='/permission-denied')
def create_employee_profile(request, id=None):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = TeacherProfileEditForm(request.POST)
        # print(profile_form)
        if user_form.is_valid() and profile_form.is_valid():
            # # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # # Set the chosen password
            # new_user.set_password(
            # user_form.cleaned_data['password'])
            # # Save the User object

            new_user.save()
            role = profile_form.cleaned_data.pop('role')
            new_user.groups.set([role])
            new_profile = profile_form.save(commit=False)
            new_profile.user_name = new_user
            new_profile.name = EmployeeInfo.objects.get(id=id)
            new_profile.save()

            return render(request,
                          'staff_mgmt/create_profile_done.html',
                          )

    else:
        user_form = CustomUserCreationForm()
        profile_form = TeacherProfileEditForm()
    return render(request,
                  'staff_mgmt/create_profile.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
