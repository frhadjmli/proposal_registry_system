from django.urls import path
from document import views

urlpatterns = [
    path('submit_proposal/', views.submit_proposal),
    path('proposal_maker/', views.proposal_maker),
    path('view_proposal/', views.view_proposal),
]
