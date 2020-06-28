from django.db import models
from django.db.models import CASCADE
from django.urls import reverse

from academy.models import Subject, Grade, Section

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


class Student(models.Model):
    father_id = models.ForeignKey(Father, related_name='stu_father', on_delete=CASCADE)
    mother_id = models.ForeignKey(Mother, related_name='stu_mother', on_delete=CASCADE)
    guardian_id = models.ForeignKey(Guardian, related_name='stu_guardian', on_delete=CASCADE)
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


class StudentProfile(models.Model):
    stu = models.OneToOneField(Student, on_delete=CASCADE, related_name='stu_profile')
    grade = models.ForeignKey(Grade, on_delete=CASCADE, related_name='stu_grade')
    section = models.ForeignKey(Section, on_delete=CASCADE, related_name='stu_section')
    roll_no = models.PositiveIntegerField()

    def get_absolute_url(self):
        """Returns the url to access a detail record for a Guardian."""
        return reverse('student-profile-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        stud = str(self.id)
        return stud
##################################################################################
# STUDENT MARK LIST COLLECTION MODELS
##################################################################################


class ActivityMarkType(models.Model):
    name = models.CharField(max_length=30)
    subject = models.ForeignKey(Subject, on_delete=CASCADE)
    grade = models.ForeignKey(Grade, on_delete=CASCADE)
    out0f = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class StudentActivityMark(models.Model):
    student_profile = models.ForeignKey(StudentProfile, on_delete=CASCADE, related_name='student_profile', default='')
    subject = models.ForeignKey(Subject, on_delete=CASCADE, related_name='student_subject', default='')
    grade = models.ForeignKey(Grade, on_delete=CASCADE, related_name='student_grade', default='')
    section = models.ForeignKey(Section, on_delete=CASCADE, related_name='student_section', default='')
    mark2 = models.PositiveIntegerField()
    mark3 = models.PositiveIntegerField()
    mark4 = models.PositiveIntegerField()
    mark5 = models.PositiveIntegerField()
    mark6 = models.PositiveIntegerField()
    mark7 = models.PositiveIntegerField()
    mark8 = models.PositiveIntegerField()
    mark19 = models.PositiveIntegerField()
    mark20 = models.PositiveIntegerField()
    subject_teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.student_profile


class StudentMark(models.Model):
    student_mark = models.ForeignKey(StudentActivityMark, on_delete=CASCADE, related_name='stu_activity_mark')
    semester = models.PositiveIntegerField()
    subject = models.ManyToManyField(Subject)
    grade = models.ManyToManyField(Grade)
    out_of_40 = models.PositiveIntegerField()
    out_of_60 = models.PositiveIntegerField()
    out_of_100 = models.PositiveIntegerField()

    def __str__(self):
        return self.student_mark


class StudentTotalMark(models.Model):
    student_total_mark = models.ForeignKey(StudentMark, on_delete=CASCADE, related_name='stu_mark')
    semester = models.PositiveIntegerField()
    grade = models.ManyToManyField(Grade)
    section = models.ManyToManyField(Section)
    subject1 = models.OneToOneField(Subject, on_delete=CASCADE, related_name='subject1')
    subject2 = models.OneToOneField(Subject, on_delete=CASCADE, related_name='subject2')
    subject3 = models.OneToOneField(Subject, on_delete=CASCADE, related_name='subject3')
    subject4 = models.OneToOneField(Subject, on_delete=CASCADE, related_name='subject4')
    subject5 = models.OneToOneField(Subject, on_delete=CASCADE, related_name='subject5')
    subject6 = models.OneToOneField(Subject, on_delete=CASCADE, related_name='subject6')
    subject7 = models.OneToOneField(Subject, on_delete=CASCADE, related_name='subject7')
    subject8 = models.OneToOneField(Subject, on_delete=CASCADE, related_name='subject8')
    subject9 = models.OneToOneField(Subject, on_delete=CASCADE, related_name='subject9')
    total = models.PositiveIntegerField()
    average = models.PositiveIntegerField()
    rank = models.PositiveIntegerField()

    def __str__(self):
        return self.student_total_mark

