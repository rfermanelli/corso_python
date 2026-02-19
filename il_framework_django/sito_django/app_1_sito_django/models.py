from django.db import models

# Create your models here.
class Studente(models.Model):
    matricola = models.CharField(max_length=5)
    nome = models.CharField(max_length=25)
    cognome = models.CharField(max_length=50)
    

class Corso(models.Model):
    codice = models.CharField(max_length=5)
    denominazione = models.CharField(max_length=20)
