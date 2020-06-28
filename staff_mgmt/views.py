from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import EmployeeInfo


class EmployeeCreateView(CreateView):
    model = EmployeeInfo
    fields = '__all__'
    success_url = reverse_lazy('list_employee')
    template_name = 'staff_mgmt/add_employee.html'

    # def get_context_data(self, **kwargs):
    #     context = super(EmployeeCreateView, self).get_context_data(**kwargs)
    #     context['employees'] = EmployeeInfo.objects.order_by('name')
    #     return context


class EmployeeUpdateView(UpdateView):  # new
    model = EmployeeInfo
    template_name = 'staff_mgmt/add_employee.html'
    fields = '__all__'
    # success_url = reverse_lazy('list_employee')


class EmployeeListView(ListView):
    model = EmployeeInfo
    template_name = 'staff_mgmt/list_employee.html'
    paginate_by = 20


class EmployeeDetailView(DetailView):
    model = EmployeeInfo
    template_name = 'staff_mgmt/employee_detail.html'
