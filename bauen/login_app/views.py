from django.shortcuts import render
from django.http import HttpResponse

def auth_user(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        return redirect('/signup')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('/dashboard')

def login(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    
    if request.method == 'POST':
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            return redirect('/signup')


def signout(request):
    logout(request)
    return redirect('/signup')