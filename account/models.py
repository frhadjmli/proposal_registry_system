from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


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
    class WorkingArea(models.TextChoices):
        instructor = 'I', 'instructor'
        assistant_professor = 'AiP', 'assistant_professor'
        associate_professor = 'AoP', 'associate_professor'
        full_professor = 'FP', 'full_professor'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    academic_rank = models.CharField(max_length=3, choices=WorkingArea.choices)
    working_area = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.get_full_name()

    def full_name(self):
        return self.user.get_full_name()


class HOD(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()


class DprtAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()
