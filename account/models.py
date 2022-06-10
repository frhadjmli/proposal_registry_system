from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class UserTypeChoice(models.TextChoices):
        student = 'ST', 'student'
        supervisor = 'SU', 'supervisor'
        HOD = 'HOD', 'HeadOfDepartment'
        DprtAdmin = 'DA', 'DepartmentAdmin'
        admin = 'A', 'admin'

    user_type = models.CharField(max_length=3, choices=UserTypeChoice.choices, null=True, blank=True)

    def __str__(self):
        return self.username

    def get_user_type(self):
        return self.user_type


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    std_number = models.CharField(max_length=10)
    field = models.CharField(max_length=50)
    taken_unit = models.PositiveIntegerField()
    passed_unit = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.get_full_name()} std_number : {self.std_number}"

    def full_name(self):
        return self.user.get_full_name()


class Supervisor(models.Model):
    class AcademicRankChoice(models.TextChoices):
        instructor = 'I', 'instructor'
        assistant_professor = 'AiP', 'assistant_professor'
        associate_professor = 'AoP', 'associate_professor'
        full_professor = 'FP', 'full_professor'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    academic_rank = models.CharField(max_length=3, choices=AcademicRankChoice.choices)
    working_area = models.CharField(max_length=100, null=True)
    capacity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.user.get_full_name()

    def full_name(self):
        return self.user.get_full_name()


class HOD(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "HOD"

    def __str__(self):
        return self.user.get_full_name()


class DprtAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "DprtAdmin"

    def __str__(self):
        return self.user.get_full_name()
