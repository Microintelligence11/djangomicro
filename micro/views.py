from django.shortcuts import render
from django.http import HttpResponse
from . models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "index.html")
    
def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")

def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        cservices = request.POST.get('cservices')
        textarea = request.POST.get('textarea')

        if len(name) <2  or len(email) <10 or len(number) < 10 or len(textarea) < 10:
            messages.error(request, "pleces fill the form correctly.")
        else:
            contact = Contact(name=name, email=email, number=number, cservices=cservices, textarea=textarea)
            contact.save()
            messages.success(request,"your form has been submitted sucessfuly")
    return render(request, "contact.html")