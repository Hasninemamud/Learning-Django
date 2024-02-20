from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def service(request):
    return render(request, "service.html")

def userfrom(request):
    try:
        # n1=request.GET['num1']
        # n2=request.GET['num2']
        n1=request.GET.get('num1')
        n2=request.GET.get('num2')
        print(n1+n2)
    except:
        pass
    return render(request, "userfrom.html")