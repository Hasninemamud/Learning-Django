from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, "index.html")

def timesanddate(request):
    return render(request, "calender.html")

def fblogin(request):
    login={
        'fb' : 'Facebook log in',
        'text': ['C', 'C++', 'PYTHON']

    }
    return render(request, "calculator.html", login)