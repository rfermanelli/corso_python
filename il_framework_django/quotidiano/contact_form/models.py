from django.db import models

# Create your models here.
class Contatto(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.EmailField()
    testo = models.TextField()
