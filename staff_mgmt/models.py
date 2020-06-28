from django.db import models
from django.urls import reverse

MARITAL_STATUS = (
    ('1', 'SINGLE'),
    ('2', 'MARRIED'),
    ('3', 'DIVORCED'),
    ('4', 'WIDOWED'),
)
GENDER_CHOICE = (
    ('1', 'MALE'),
    ('2', 'FEMALE'),

)
REGION_CHOICE = (
    ('1', 'ZOBA ANSEBA'),
    ('2', 'ZOBA DEBUB'),
    ('3', 'ZOBA GASH BARKA'),
    ('4', 'ZOBA NORTHER RED SEA'),
    ('5', 'ZOBA MAEKEL'),
    ('6', 'ZOBA SOUTHER RED SEA'),


)


class EmployeeInfo(models.Model):
    first_name = models.CharField(max_length=40)
    father_name = models.CharField(max_length=40)
    grand_father_name = models.CharField(max_length=40)
    gender = models.CharField(choices=GENDER_CHOICE,max_length=5 )
    birth_date = models.DateField(default='1990-01-25')
    marital_status = models.CharField(choices=MARITAL_STATUS,
                                      default='SINGLE',max_length=5)
    children = models.PositiveSmallIntegerField()
    national_id = models.CharField(max_length=50)
    asc_code = models.CharField(max_length=40, unique=True)
    employee_image = models.ImageField(upload_to='portfolio/staff/images')
    region = models.CharField(choices=REGION_CHOICE, max_length=5)
    sub_region = models.CharField(max_length=30)
    permanent_address = models.CharField(max_length=50)
    present_address = models.CharField(max_length=50)
    religion = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    resume = models.FileField(upload_to='portfolio/staff/docs/', null= True)
    gpa = models.DecimalField(decimal_places=3, max_digits=6)
    job_type = models.CharField(max_length=40)
    experience = models.CharField(max_length=40)
    joining_date = models.DateField(auto_now_add=True)
    disability = models.CharField(max_length=200)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return str(self.first_name + self.father_name)

    def get_absolute_url(self):  # new
        return reverse('employee_details', args=[str(self.id)])



class EmployeeStatus(models.Model):
    name = models.OneToOneField(EmployeeInfo, on_delete=models.CASCADE)
    employee_role = models.CharField(max_length=40)
    salary = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
