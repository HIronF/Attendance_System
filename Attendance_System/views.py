from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
def base(request):
    return render(request, 'base.html')

def user_login(request):  # Renamed the view function
    return render(request, 'login.html')

def dologin(request):
    if request.method == 'POST':
        user = EmailBackend.authenticate(request,username=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                pass
            elif user_type == '3':
                pass
            else:
                # Message
                return render(request, 'login')
        else:
            return render(request, 'login')


def doLogout(request):
    logout(request)
    return redirect('user_login')


def Profile(request):
    return render(request, 'profile.html')