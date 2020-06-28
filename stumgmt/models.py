from django.db import models
from django.db.models import CASCADE, PROTECT
from django.urls import reverse

ZOBA = [
    ('MAEKEL', 'MAEKEL'),
    ('SOUTHERN', 'SOUTHERN'),
    ('GASH-BARKA', 'GASH-BARKA'),
    ('ANSEBA', 'ANSEBA'),
    ('NORTHERN-RED-SEA', 'NORTHERN-RED-SEA'),
    ('SOUTHERN-RED-SEA', 'SOUTHERN-RED-SEA'),
]
RELIGION = [
    ('CHRISTIAN', 'CHRISTIAN'),
    ('MUSLIM', 'MUSLIM'),
]

GENDER = [
    ('F', 'FEMALE'),
    ('M', 'MALE')
]
ETHNICITY = [
    ('TIGRIGNA', 'TIGRIGNA'),
    ('TIGRE', 'TIGRE'),
    ('SAHO', 'SAHO'),
    ('BILEN', 'BILEN'),
    ('AFAR', 'AFAR'),
    ('NARA', 'NARA'),
    ('KUNAMA', 'KUNAMA'),
    ('HIDAREB', 'HIDAREB'),
    ('RASHAIDA', 'RASHAIDA')
]


# Create your models here.
# Student Model
class Father(models.Model):
    f_first_name = models.CharField(max_length=255)
    f_middle_name = models.CharField(max_length=255)
    f_last_name = models.CharField(max_length=255)
    f_pic = models.ImageField(blank=True)
    f_ASC = models.PositiveIntegerField()
    f_zoba = models.CharField(max_length=20, choices=ZOBA)
    f_sub_zoba = models.CharField(max_length=255, blank=True)
    f_religion = models.CharField(max_length=10, choices=RELIGION)
    f_phone_no = models.IntegerField(blank=True)
    f_occupation = models.CharField(max_length=255, blank=True)
    f_is_guardian = models.BooleanField(blank=True)

    def __str__(self):
        return self.f_first_name

    def get_absolute_url(self):
        """Returns the url to access a detail record for a mother."""
        return reverse('father-detail', args=[str(self.id)])


class Mother(models.Model):
    m_first_name = models.CharField(max_length=255)
    m_middle_name = models.CharField(max_length=255)
    m_last_name = models.CharField(max_length=255)
    m_mother_pic = models.ImageField(blank=True)
    m_ASC = models.PositiveIntegerField()
    m_zoba = models.CharField(max_length=20, choices=ZOBA)
    m_sub_zoba = models.CharField(max_length=255)
    m_religion = models.CharField(max_length=10, choices=RELIGION)
    m_phone_no = models.PositiveIntegerField(blank=True)
    m_occupation = models.CharField(max_length=255, blank=True)
    m_is_guardian = models.BooleanField()

    def __str__(self):
        """String for representing the Model object."""
        return self.m_first_name

    def get_absolute_url(self):
        """Returns the url to access a detail record for a mother."""
        return reverse('mother-detail', args=[str(self.id)])


# Guardian Model
class Guardian(models.Model):
    g_first_name = models.CharField(max_length=255)
    g_middle_name = models.CharField(max_length=255)
    g_last_name = models.CharField(max_length=255)
    g_guardian_pic = models.ImageField(blank=True)
    g_ASC = models.PositiveIntegerField()
    g_gender = models.CharField(max_length=1, choices=GENDER, default='')
    g_zoba = models.CharField(max_length=20, choices=ZOBA)
    g_sub_zoba = models.CharField(max_length=255)
    g_religion = models.CharField(max_length=10, choices=RELIGION)
    g_phone_no = models.PositiveIntegerField(blank=True)
    g_occupation = models.CharField(max_length=255, blank=True)
    g_relationship = models.CharField(max_length=100, default='')
    g_is_father = models.BooleanField()
    g_is_mother = models.BooleanField()
    g_is_guardian = models.BooleanField()

    def __str__(self):
        """String for representing the Model object."""
        return self.g_first_name

    def get_absolute_url(self):
        """Returns the url to access a detail record for a Guardian."""
        return reverse('guardian-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.g_first_name


class StudentProfile(models.Model):
    stu = models.OneToOneField('Student', on_delete=CASCADE, related_name='stu_profile')
    grade = models.PositiveIntegerField()
    section = models.PositiveIntegerField()
    roll_no = models.PositiveIntegerField()

    def get_absolute_url(self):
        """Returns the url to access a detail record for a Guardian."""
        return reverse('student-profile-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        stud = str(self.id)
        return stud


class Student(models.Model):
    father_id = models.ForeignKey('Father', related_name='stu_father', on_delete=CASCADE)
    mother_id = models.ForeignKey('Mother', related_name='stu_mother', on_delete=CASCADE)
    guardian_id = models.ForeignKey('Guardian', related_name='stu_guardian', on_delete=CASCADE)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    student_pic = models.CharField(max_length=255)
    ASC = models.IntegerField()
    zoba = models.CharField(max_length=20, choices=ZOBA)
    sub_zoba = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    religion = models.CharField(max_length=10, choices=RELIGION)
    gender = models.CharField(max_length=1, choices=GENDER)
    birth_place = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=10, choices=ETHNICITY)
    DOB = models.DateField()
    admission_date = models.DateField()

    def __str__(self):
        """String for representing the Model object."""
        return self.first_name

    def get_absolute_url(self):
        """Returns the url to access a detail record for a student."""
        return reverse('student-detail', args=[str(self.id)])

##################################################################################
# STUDENT MARK LIST COLLECTION MODELS
##################################################################################


class ActivityMarkType(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    grade = models.PositiveIntegerField()
    out0f = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class StudentActivityMark(models.Model):
    student = models.ForeignKey('Student', on_delete=CASCADE, related_name='student')
    activity = models.ForeignKey('ActivityMarkType', on_delete=CASCADE, related_name='stu_activity')
    subject = models.CharField(max_length=100)
    grade = models.PositiveIntegerField()
    section = models.PositiveIntegerField()
    result = models.PositiveIntegerField()
    subject_teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.student


class StudentMark(models.Model):
    student = models.ForeignKey('StudentActivityMark', on_delete=CASCADE, related_name='stu_activity_mark')
    semester = models.PositiveIntegerField()
    grade = models.PositiveIntegerField()
    subject = models.CharField(max_length=100)
    out_of_40 = models.PositiveIntegerField()
    out_of_60 = models.PositiveIntegerField()
    out_of_100 = models.PositiveIntegerField()

    def __str__(self):
        return self.student


class StudentTotalMark(models.Model):
    student = models.ForeignKey('StudentMark', on_delete=CASCADE, related_name='stu_mark')
    semester = models.PositiveIntegerField()
    grade = models.PositiveIntegerField()
    section = models.PositiveIntegerField()
    sub1 = models.CharField(max_length=100)
    sub2 = models.CharField(max_length=100)
    sub3 = models.CharField(max_length=100)
    sub4 = models.CharField(max_length=100)
    sub5 = models.CharField(max_length=100)
    sub6 = models.CharField(max_length=100)
    sub7 = models.CharField(max_length=100)
    sub8 = models.CharField(max_length=100)
    sub9 = models.CharField(max_length=100)
    total = models.PositiveIntegerField()
    average = models.PositiveIntegerField()
    rank = models.PositiveIntegerField()

    def __str__(self):
        return self.student

