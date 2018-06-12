from django.db import models
from django.utils import timezone


class Batiment(models.Model):

    nom = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nom

class Logiciel(models.Model):
	
    nom = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nom

class Version(models.Model):
	
    nom = models.TextField()
    logiciel = models.ForeignKey(Logiciel, on_delete=models.CASCADE,default=0)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nom

class Demande(models.Model):

    nom = models.CharField(max_length=100,default='Unknown')
    prenom = models.CharField(max_length=100,default='Unknown')
    email = models.EmailField(max_length=100,default='Unknown')
    phone = models.CharField(max_length=10,default='Unknown')
    batiment = models.ForeignKey(Batiment, on_delete=models.CASCADE,default=0)
    bureau = models.CharField(max_length=100,default='Unknown')
    logiciel = models.ForeignKey(Logiciel, on_delete=models.CASCADE,default=0)
    version = models.ForeignKey(Version, on_delete=models.CASCADE,default=0)
    os = models.CharField(max_length=50)
    host = models.CharField(max_length=17)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nom