from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse, reverse_lazy
from staff_mgmt.models import EmployeeStatus



class Grade(models.Model):
    GRADE_CHOICES = [(i, str(i)) for i in range(1, 13)]
    grade = models.PositiveSmallIntegerField(unique=True,
                                             choices=GRADE_CHOICES,
                                             default='draft')

    class Meta:
        ordering = ('grade',)

    def __str__(self):
        return str(self.grade)


class Room(models.Model):
    block = models.PositiveSmallIntegerField()
    room = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ("block", "room")
        ordering = ("block", "room")

    def __str__(self):
        return " Block : " + str(self.block) + " room : " + str(self.room)


class Section(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    section = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ("grade", "section")
        index_together = ("grade", "section")
        ordering = ('grade',)

    def __str__(self):
        return "Grade : " + str(self.grade) + " sec : " + str(self.section)

    def get_absolute_url(self):  # new
        return reverse_lazy('section')

class Subject(models.Model):
    name = models.CharField(max_length=20)
    grade = grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("name", "grade")
        ordering = ('grade',)

    def __str__(self):
        return str( self.name) + ' for grade: ' + str(self.grade)


class TeacherAssignment(models.Model):
    teacher = models.OneToOneField(EmployeeStatus, on_delete=models.CASCADE, related_name='teachers' )
    subject = models.ManyToManyField(Subject, related_name='subjects')
    Section = models.ManyToManyField(Section, related_name='classes')

    class Meta:
        ordering = ('teacher',)

    def __str__(self):
        return str(self.teacher)

    def get_absolute_url(self):  # new
        return reverse('teacher_assigned_detail', args=[str(self.id)])
