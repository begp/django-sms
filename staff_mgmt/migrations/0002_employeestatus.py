# Generated by Django 3.0.5 on 2020-06-25 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff_mgmt', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeStatus',
            fields=[
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('employee_role', models.CharField(max_length=40)),
                ('salary', models.PositiveIntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='staff_mgmt.EmployeeInfo')),
            ],
        ),
    ]
