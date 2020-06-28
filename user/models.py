from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse, reverse_lazy


class CustomUser(AbstractUser):
    pass

    class Meta:
        app_label = 'user'



    def get_absolute_url(self):
        return reverse_lazy('user_detail', args=[self.pk])
