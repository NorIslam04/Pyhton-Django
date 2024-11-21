from . import views
from django.urls import path

urlpatterns = [
    path('person', views.person, name='person'),  # name='person' is the name of the url pattern, qui est utilisé pour les liens inverses et appelé la fcntion views.person
    path('persons', views.persons, name='persons'),
]


