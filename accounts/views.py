from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout


def login_v(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('webapp:home')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


def logout_v(request):
    logout(request)
    return redirect('webapp:home')