from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def loginUser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse('Login completed!')
            # return redirect('??')

        return HttpResponse('Wrong password/username')
        # return render(request, 'login.html', {'msg': 'Wrong password/username'})

    return HttpResponse('Please login with post method')
    # return render(request, 'login.html')

@csrf_exempt
def logoutUser(request):

    if not request.user.is_authenticated:
        return HttpResponse('Please login first')
        # return redirect('login')

    logout(request)
    return HttpResponse('Logout successfully')
    # return redirect('login')
