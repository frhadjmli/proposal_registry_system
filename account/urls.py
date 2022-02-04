from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('group_up/', views.group_up, name='group_up'),
    path('supervisors_list/', views.supervisors_list, name='supervisors_list'),
    path('supervisor_profile/', views.supervisor_profile, name='supervisor_profile'),
    path('hod_profile/', views.hod_profile, name='hod_profile'),
    path('req_to_lecturer/', views.req_to_lecturer, name='req_to_lecturer'),
]
# use option name in return redirect() in views.py
# use option name in {% url 'logout'%} in student_profile.html
