from django.urls import path
from django.contrib.auth import views as auth_views

from .views import RegisterView, HomeView, ListUsersView, UserInfoView, change_pwd

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('<int:id>', change_pwd, name='reset-pwd'),
    path('login/', auth_views.LoginView.as_view( redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('users/<int:pk>', UserInfoView.as_view(), name='user_detail'),
    path('list/', ListUsersView.as_view(), name='list_all'),

    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

]
