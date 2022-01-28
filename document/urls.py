from django.urls import path
from document.views import submit_proposal

urlpatterns = [
    path('submit/', submit_proposal),
]