from django.shortcuts import render
from django.http import HttpResponse
from document.models import Proposal
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def submit_proposal(request):
    if request.method == 'POST':
        try:
            proposal = Proposal()
            proposal.title = request.POST.get('...')
            proposal.supervisor = request.POST.get('...')
            proposal.student = request.POST.get('...')
            proposal.semester = request.POST.get('...')
            proposal.academic_year = request.POST.get('...')
            proposal.summary = request.POST.get('...')
            proposal.message = None
            proposal.save()
            response = "Proposal added Successfuly to database."
            return HttpResponse(response)
        except:
            response = "Proposal failed to add in database!"
            return HttpResponse(response)
        