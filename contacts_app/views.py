from django.shortcuts import render

from .models import Contact
# Create your views here.

def home(request):
    return render(template_name="home.html", request=request, context={"contacts":Contact.objects.all()})

def create(request):
    pass

def update(request):
    pass

def delete(request):
    pass