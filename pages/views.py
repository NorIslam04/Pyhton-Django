from django.shortcuts import render
from django.http import HttpResponse as hr


def index(req):
    return render(req,"pages/index.html")

def about(req):
    return hr("about page")
