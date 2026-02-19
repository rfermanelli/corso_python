# Importazione della funzione che ha fra i suoi argomenti il template html:
from django.shortcuts import render, get_object_or_404

# Importazione della funzione che non ha fra i suoi argomenti il template html:
from django.http import HttpResponse

# Importazione del modello dei dati:
from core.models import Articolo

# Create your views here.
# Definizione di una funzione controller che ha come parametro la variabile primary_key
# che rappresenta la chiave primaria dell'oggetto Articolo:
def articolo(request, primary_key):
    # Definizione dei dati da visualizzare nel template html:
    Articolo.objects.all().delete()
    Articolo.objects.create(titolo = "La relatività", testo = "La relatività è relativa")
    #articolo = Articolo.objects.get(id = primary_key)
    articolo = get_object_or_404(Articolo, pk = Articolo.objects.get().id)

    # Rendering che utilizza il template html:
    context = {"articolo": articolo}
    return render(request, "articolo.html", context)

    # Rendering che non utilizza il template html:
    # return HttpResponse(f"{articolo}")

def dettaglio_articolo(request):
    articolo = Articolo.objects.all()
    # Rendering che utilizza il template html:
    context = {"articolo": articolo}
    return render(request, "dettaglio_articolo.html", context)

    # Rendering che non utilizza il template html:
    #return HttpResponse(f"{articolo}")