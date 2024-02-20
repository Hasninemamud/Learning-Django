from django.http import HttpResponse, HttpResponsePermanentRedirect
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
    finalans=0

    try:
       
         if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2

            url="/about/?output={}".format(finalans)

            return HttpResponsePermanentRedirect(url)
    except:
        pass
    return render(request, "userfrom.html",{'output':finalans})