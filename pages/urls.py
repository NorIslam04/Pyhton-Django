from django.urls import path
from . import views

urlpatterns = [

    path('', views.index1, name='index'),
    path('about/', views.about, name='about'),
    path('test/',views.test,name='test')

]