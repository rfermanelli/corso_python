from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

models_list = [
    Dipartimento,
    CorsoDiLaurea,
    Docente,
    Corso,
    Studente,
    AppelloEsame,
    PrenotazioneEsame,
    PianoDiStudi,
    IscrizioneAnnuale,
]

for model in models_list:
    admin.site.register(model)
