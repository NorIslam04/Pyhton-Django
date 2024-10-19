from django.shortcuts import render


def index1(req):

    x={'name': 'Islam Aoudia Nour', 'age' :""}

    return render(req,"pages/index.html",x)

def about(req):
    return render(req,"pages/about.html")

def test(req):
    return render(req,"pages/test.html")
