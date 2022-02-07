from django.urls import path
from document import views

urlpatterns = [
    path('submit_proposal/', views.submit_proposal, name='submit_proposal'),
    path('view_proposal/', views.view_proposal, name='view_proposal'),
]
