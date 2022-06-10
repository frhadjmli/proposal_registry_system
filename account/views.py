from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from account.models import User, Supervisor
from .decorators import student_required, supervisor_required, hod_required, dprt_admin_required
from document.models import Proposal
"""
آن دسته از ویوو های که اضافه کامنت گذاری شدن فعلا در اولویت نیستند
"""


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print()
            if user.user_type == 'ST':
                return redirect('student_profile')
            elif user.user_type == 'SU':
                return redirect('supervisor_profile')
            elif user.user_type == 'HOD':
                return redirect('hod_profile')
            elif user.user_type == 'DA':
                return redirect('/admin/')  # redirect to admin panel
            else:
                print("user_type is null")
                return redirect('logout')

        return render(request, 'account/login.html', {'msg': 'Wrong password/username'})

    return render(request, 'account/login.html')


@student_required
@login_required
def student_profile(request):
    proposal = Proposal.objects.filter(student__user=request.user)
    print(proposal)
    return render(request, 'account/student_profile.html', {'proposal': proposal})


def logout_user(request):

    if not request.user.is_authenticated:
        # return HttpResponse('Please login first')
        return redirect('login')

    logout(request)
    return redirect('login')


# با زدن دکمه ایجاد گروه به اینجا درخواست میزنیم
@student_required
@login_required
def group_up(request):
    return render(request, 'account/group_up.html')


# با زدن دکمه لیست اساتید به اینجا ریکویست میزنیم
@student_required
@login_required
def supervisors_list(request):
    supervisors = Supervisor.objects.select_related('user')
    print(supervisors)
    return render(request, 'account/supervisors_list.html', {'supervisors':supervisors})


# در صفحه لاگین اگر نوع کاربر استاد راهنما باشد به این صفحه درخواست میزنیم
@supervisor_required
@login_required
def supervisor_profile(request):
    full_name = request.user.get_full_name()
    proposal = Proposal.objects.filter(supervisor__user=request.user)
    return render(request, 'account/supervisor_profile.html', {'full_name': full_name, 'proposal': proposal})


# اگر نوع کاربر پس از درخواست در صفحه لاگین مدیر گروه باشد به این صفحه ریکویست میدهیم
@hod_required
@login_required
def hod_profile(request):
    return render(request, 'account/hod_profile.html')


# با کلیک بر روی نام استادها در لیست اساتید با این ریکوعست صفحه پیش نمایش پروفایل استاد را میگیریم
@student_required
@login_required
def req_to_lecturer(request):  # اضافه
    return render(request, 'account/req_to_lecturer.html')


# با زدن دکمه یادداشت برای استاد این صحفه را می آوریم
def note_to_supervisor(request):  # اضافه
    return render(request, 'account/note_to_supervisor.html')
