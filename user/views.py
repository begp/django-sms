from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, DetailView, TemplateView

from .forms import CustomUserCreationForm, UserPassChangeForm
from .models import CustomUser



class RegisterView(CreateView):
    login_url = 'login'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class ListUsersView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'user/list_users.html'
    # paginate_by = 4
    context_object_name = 'users'


class UserInfoView(LoginRequiredMixin, DetailView):
    # model = CustomUser
    queryset = CustomUser.objects.select_related()
    template_name = 'user/detail.html'
    context_object_name = 'users'


def change_pwd(request, id):
    if request.method == "POST":
        form = UserPassChangeForm(request.POST)
        if form.is_valid():
            p = form.cleaned_data["new_password1"]
            # password = request.POST.get("new_password1")
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
