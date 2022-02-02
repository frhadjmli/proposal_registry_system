"""this file handles all the logic around proposal
'submit_proposal(request)' is responsible for showing the proposal form to the student and also
get all the data and save it in DB."""

from django.shortcuts import render
from django.http import HttpResponse
from document.models import Proposal
from django.views.decorators.csrf import csrf_exempt
from document.forms import ProposalForm


# Create your views here.
def submit_proposal(request):
    if request.method == 'GET':
        form = ProposalForm()
        return render(request, 'document/submit_proposal.html', {'form': form})  # xxx.html should replace with real one
    if request.method == 'POST':
        try:
            form = ProposalForm(request.POST)
            if form.is_valid():
                form.save()
                response = "Proposal added Successfully to database."
                return HttpResponse(response)
            else:
                response = "Proposal form is not valid!"
                return HttpResponse(response)
        except:
            response = "Proposal failed to add in database!"
            return HttpResponse(response)


# با زدن دکمه ساخت پروپوزال و ارسال این ریکوعست صفحه ساخت پروپوزال را باز میکنیم
def proposal_maker(request):
    return render(request, 'document/proposal_maker.html')


# با کلیک بر روی نمایش پروپوزال با این ویوو پروپوزال نمایش داده میشود ولی دکمه سابمیت فقط برای دانشجو بر حسب شرط می آید
def view_proposal(request):
    return render(request, 'document/view_proposal.html')


