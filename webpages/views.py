from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request,'homepage/homepage.html')


def aboutpage(request):
    return render(request,'aboutpage/aboutpage.html')

def servicepage(request):
    return render(request,'servicepage/servicepage.html')

def contactus(request):
    return render(request,'contactus/contactus.html')