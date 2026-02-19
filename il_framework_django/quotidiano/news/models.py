from django.db import models

# Create your models here.
class Giornalista(models.Model):
    nome = models.CharField(max_length=25)
    cognome = models.CharField(max_length=50)


class Articolo(models.Model):
    titolo = models.CharField(max_length=50)
    testo = models.TextField(max_length=1000, default="")
