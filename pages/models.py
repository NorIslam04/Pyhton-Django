from django.db import models

#creation d'un tableau de données

class Preson(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    job = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self): #methode qui permet de retourner le nom de la personne
        return self.name
    
    
    
    