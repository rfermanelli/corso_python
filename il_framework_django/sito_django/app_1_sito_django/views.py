from django.shortcuts import render
from django.http import HttpResponse
from app_1_sito_django.models import Studente

# Create your views here.
def homepage(request):
    stringa_di_output = "<!DOCTYPE html> <html> <head> <title>La mia pagina semplice</title> </head> <body> <h1>Benvenuto nella mia pagina!</h1> <p>Questa è una pagina HTML statica molto semplice.</p> <p>Contiene solo gli elementi base:</p> <ul> <li>Un titolo</li> <li>Alcuni paragrafi</li> <li>Una lista</li> </ul> </body> </html>"
    return HttpResponse(stringa_di_output)


def chi_siamo(request):
    return HttpResponse("Siamo il gruppo Python")

