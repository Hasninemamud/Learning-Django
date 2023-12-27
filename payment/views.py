from django.shortcuts import render

# Create your views here.
def bkash(request):
    return render(request, 'payment/payment-1.html')

def rocket(request):
    return render(request, 'payment/payment-2.html')