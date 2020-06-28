from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, DetailView, TemplateView

from .forms import CustomUserCreationForm, UserPassChangeForm
from .models import CustomUser


class RegisterView(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    login_url = 'login'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/create_profile.html'
    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class ListUsersView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'user/list_users.html'
    # paginate_by = 4
    context_object_name = 'users'


class UserInfoView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = CustomUser

    # queryset = user.objects.select_related()
    template_name = 'user/detail.html'
    context_object_name = 'users'
    def test_func(self):
        group = Group.objects.get(name='director')
        return True if group in self.request.user.groups.all() else False
    # def get_context_data(self, **kwargs):
    #
    #     context = super(UserInfoView, self).get_context_data(**kwargs)
    #     context['xxx'] = self.model.objects.select_related('profile').get(id=2)
    #     return context

def user_access_check(user):
    group = Group.objects.get(name='director')
    return True if group in user.groups.all() else False






@login_required
@user_passes_test(user_access_check, redirect_field_name='/permission-denied')
def change_pwd(request, id):
    if request.method == "POST":
        form = UserPassChangeForm(request.POST)
        if form.is_valid():
            p = form.cleaned_data["new_password1"]
            user = get_user_model()
            user = user.objects.get(id=id)

            user.set_password(p)
            user.save()

            return HttpResponse("Menu Successfully created")
        else:

            messages.error(request, 'Something went wrong')
    user_form = UserPassChangeForm()
    users = get_user_model()
    users = users.objects.get(id=id)
    return render(request,
                  'user/custom_password_reset.html',
                  {'user_form': user_form,
                   'user': users.username, })
