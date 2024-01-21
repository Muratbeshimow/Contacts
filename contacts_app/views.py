from django.shortcuts import render

from .models import Contact
# Create your views here.

def home(request):
    return render("home.html", {"contacts":Contact.objects.all()})

def create(request):
    pass

def update(request):
    pass

def delete(request):
    pass