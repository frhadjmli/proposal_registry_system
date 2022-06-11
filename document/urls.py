from django.urls import path
from document import views

urlpatterns = [
    path('submit_proposal/', views.submit_proposal, name='submit_proposal'),
    path('view_proposal/<int:pk>/', views.view_proposal, name='view_proposal'),
    path('accept_proposal/<int:pk>/', views.accept_proposal, name='accept_proposal'),
]
