from django.apps import AppConfig
from django.db import models


class UserConfig(AppConfig):
    name = 'user'


# class Mymodel2(models.Model):
#     model1 = models.ForeignKey(app1.mymodel1)
