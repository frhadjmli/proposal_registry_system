from django.db import models
from account.models import Student, Supervisor

# Create your models here.
class Proposal(models.Model):

    STATUS_CHOICES = {

        ('pen', 'pending'),
        ('rsup', 'rejected by supervisor'),
        ('asup', 'accepted by supervisor'),
        ('radm', 'rejected by admin'),
        ('aadm', 'accepted by admin'),
        ('rhod', 'rejected by HOD'),
        ('ahod', 'accepted by HOD'),
    }

    title = models.CharField(max_length=100)
    supervisor = models.ManyToManyField(Supervisor)
    student = models.ManyToManyField(Student)
    semester = models.CharField(max_length=3) # e.g:'اول' یا 'دوم'
    academic_year = models.CharField(max_length=4) # e.g:'1400'
    summary = models.TextField(null=False, help_text="مختصر اطلاعاتی درباره پروپزال")
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='pen')

    def get_supervisors(self):
        return "\n".join([superv.full_name() for superv in self.supervisor.all()])

    def get_students(self):
        return "\n".join([std.full_name() for std in self.student.all()])
   
    def __str__(self):
        return self.title

class Message(models.Model):

    title = models.CharField(max_length=50, null=True)
    sender = models.ForeignKey(Supervisor, on_delete=models.DO_NOTHING)
    text = models.TextField(null=True, help_text="پیام خود را وارد کنید.")
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE, null=True)

