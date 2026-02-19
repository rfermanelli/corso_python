# Importazione della funzione del modello:
from django.db import models

# Create your models here.
# Definizione del modello dei dati della entità Articolo:
class Articolo(models.Model):
    titolo = models.CharField(max_length=50)
    testo = models.TextField(max_length=1000, default="")

    def __str__(self):
        return f"{self.titolo}, {self.testo}"