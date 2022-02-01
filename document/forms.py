from dataclasses import fields
from pyexpat import model
from document.models import Proposal
from django import forms

class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ('title', 'supervisor', 'student', 'semester', 
        'academic_year', 'summary') # did not mention 'message' and 'status' because those are irrelevant