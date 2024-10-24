from django.shortcuts import render

# Create your views here.

def person(request):
    return render(request, 'person/person.html')

def persons(request):
    return render(request, 'person/persons.html')