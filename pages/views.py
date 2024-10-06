from django.shortcuts import render
from django.http import HttpResponse as hr

def index(req):
    return hr("hello Hero")

