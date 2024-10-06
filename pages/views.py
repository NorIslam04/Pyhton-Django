from django.shortcuts import render
from django.http import HttpResponse as hr


def index(req):
    x={'name': 'Islam Aoudia Nour', 'age' :""}
    return render(req,"pages/index.html",x)

def about(req):
    return render(req,"pages/about.html")
