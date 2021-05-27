from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    my_dict = {'insert': 'Im the login context'}
    return render(request, 'bauen/templates/login.html', context=my_dict)
