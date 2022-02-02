from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logoutUser),
    path('student_profile/', views.student_profile),
    path('group_up/', views.group_up),
    path('supervisors_list/', views.supervisors_list),
    path('supervisor_profile/', views.supervisor_profile),
    path('hod_profile/', views.hod_profile),
]
