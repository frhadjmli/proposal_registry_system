"""this file handles all the logic around proposal
'submit_proposal(request)' is responsible for showing the proposal form to the student and also
get all the data and save it in DB."""

from django.shortcuts import render
from django.http import HttpResponse
from document.models import Proposal
from account.models import Student, Supervisor
from django.views.decorators.csrf import csrf_exempt
from document.forms import ProposalForm
from django.core.exceptions import ValidationError



# Create your views here.
def submit_proposal(request):
    if request.method == 'GET':
        return render(request, 'document/proposal_maker.html')
    if request.method == 'POST':
        try:
            
            user_data = {'supervisor':[], 'student':[]}
            
            user_data['title'] = request.POST.get('title')
            user_data['academic_year'] = request.POST.get('academic_year')
            user_data['semester'] = request.POST.get('semester')
            user_data['summary'] = request.POST.get('summary')
            supervisors_fullnames = request.POST.get('supervisor')
            students_fullnames = request.POST.get('student')
           
            
            
            for fullname in supervisors_fullnames.split('-'):
                # supervisor = Supervisor.objects.get(user__get_full_name=fullname)
                supervisors = Supervisor.objects.all()
                for supervisor in supervisors:
                    longname = supervisor.user.get_full_name()
                    if longname == fullname:
                        user_data['supervisor'].append(supervisor.id)
           
            for fullname in students_fullnames.split('-'):
                #student = Student.objects.get(user__get_full_name=fullname)
                students = Student.objects.all()
                for student in students:
                    longname = student.user.get_full_name()
                    if longname == fullname:
                        user_data['student'].append(student.id)
            
            form = ProposalForm(user_data)
            if form.is_valid():
                form.save()
                response = "Proposal added Successfully to database."
                return HttpResponse(response)
            else:
                response = "Proposal form is not valid!"
                return HttpResponse(response)
        except ValidationError:
            response = "Proposal failed to add in database!"
            return HttpResponse(response)


# با زدن دکمه ساخت پروپوزال و ارسال این ریکوعست صفحه ساخت پروپوزال را باز میکنیم
def proposal_maker(request):
    return render(request, 'document/proposal_maker.html')


# با کلیک بر روی نمایش پروپوزال با این ویوو پروپوزال نمایش داده میشود ولی دکمه سابمیت فقط برای دانشجو بر حسب شرط می آید
def view_proposal(request):
    return render(request, 'document/view_proposal.html')


