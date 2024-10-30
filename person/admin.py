from django.contrib import admin
from .models import Person
from.models import Post
# Register your models here.
#les chose qui affiche dans l'admin panel

admin.site.register(Person)
admin.site.register(Post)
