from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    bio = models.TextField()
    image = models.ImageField(upload_to='photos/%Y%m%d')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        ordering = ['first_name'] #trie les personnes par ordre alphabetique
        verbose_name_plural = 'People' #change le nom de la table dans l'admin
