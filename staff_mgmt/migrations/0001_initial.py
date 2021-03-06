# Generated by Django 3.0.5 on 2020-06-25 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('father_name', models.CharField(max_length=40)),
                ('grand_father_name', models.CharField(max_length=40)),
                ('gender', models.CharField(choices=[('1', 'MALE'), ('2', 'FEMALE')], max_length=5)),
                ('birth_date', models.DateField(default='1990-01-25')),
                ('marital_status', models.CharField(choices=[('1', 'SINGLE'), ('2', 'MARRIED'), ('3', 'DIVORCED'), ('4', 'WIDOWED')], default='SINGLE', max_length=5)),
                ('children', models.PositiveSmallIntegerField()),
                ('national_id', models.CharField(max_length=50)),
                ('asc_code', models.CharField(max_length=40, unique=True)),
                ('employee_image', models.ImageField(upload_to='portfolio/staff/images')),
                ('region', models.CharField(choices=[('1', 'ZOBA ANSEBA'), ('2', 'ZOBA DEBUB'), ('3', 'ZOBA GASH BARKA'), ('4', 'ZOBA NORTHER RED SEA'), ('5', 'ZOBA MAEKEL'), ('6', 'ZOBA SOUTHER RED SEA')], max_length=5)),
                ('sub_region', models.CharField(max_length=30)),
                ('permanent_address', models.CharField(max_length=50)),
                ('present_address', models.CharField(max_length=50)),
                ('religion', models.CharField(max_length=30)),
                ('nationality', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('resume', models.FileField(null=True, upload_to='portfolio/staff/docs/')),
                ('gpa', models.DecimalField(decimal_places=3, max_digits=6)),
                ('job_type', models.CharField(max_length=40)),
                ('experience', models.CharField(max_length=40)),
                ('joining_date', models.DateField(auto_now_add=True)),
                ('disability', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('first_name',),
            },
        ),
    ]
