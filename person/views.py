from django.shortcuts import render
from .models import Person

# Create your views here.
# function with return render(request,response,context)

def person(request):

    persons = Person.objects.filter(first_name="islam")
    if persons.exists():
        person = persons.first()

    return render(request, 'person/person.html', {'person': person})



def persons(request):
    return render(request, 'person/persons.html',{'person': Person.objects.all()})