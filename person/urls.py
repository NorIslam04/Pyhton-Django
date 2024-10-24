from . import views
from django.urls import path

urlpatterns = [
    path('person/', views.person, name='person'),
    path('', views.persons, name='persons'),
]
