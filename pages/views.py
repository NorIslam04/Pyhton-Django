from django.shortcuts import render
from django.http import HttpResponse as hr


def index(req):
    x={'name': 'islam', 'age' : 20}
    return render(req,"pages/index.html",x)

def about(req):
    return hr("about page")
