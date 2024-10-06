from django.shortcuts import render
from django.http import HttpResponse as hr


def index(req):
    return hr("index page")

def about(req):
    return hr("about page")
