from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html', {'name': 'Home page'})


def auth(request):
    login_form = AuthenticationForm()
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('main')
    context = {
        'form': login_form
    }
    return render(request, "login_form.html", context)


def session_invalidate(request):
    logout(request)
    return redirect('main')
