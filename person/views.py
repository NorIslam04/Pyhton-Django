from django.shortcuts import render
from .models import Person

# Create your views here.

def person(request):
    return render(request, 'person/person.html')

def persons(request):
    return render(request, 'person/persons.html',{'person': Person.objects.all()})