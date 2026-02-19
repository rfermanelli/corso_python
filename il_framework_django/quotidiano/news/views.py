from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

# Import del model
from news.models import Articolo, Giornalista
# Import del render
from django.shortcuts import render

# Create your views here.
def home(request):
    # Cancellazione delle tuple delle tabelle Giornalista e Articolo:
    Giornalista.objects.all().delete()
    Articolo.objects.all().delete()

    #raise Exception("VIEW ESEGUITA")

    Giornalista.objects.create(
        nome="Alan",
        cognome="Ford"
        )
    Giornalista.objects.create(
        nome="Bob",
        cognome="Rock"
        )
    Articolo.objects.create(
        titolo="Derby",
        testo=""
        )
    Articolo.objects.create(
        titolo="I tre di Yuma",
        testo=""
        )
    # art = Giornalista(nome=f"Bob{i}", cognome=f"Rock{i}")
    # art.save()
    # # Insert di un oggetto Articolo
    # art = Articolo(titolo="Il mare", testo="Il mare è bello")
    # art.save()
    # #
    # Articolo.objects.create(
    #     titolo="Il lago",
    #     testo="Il lago così così"
    # )
    # #
    # # Delete di un oggetto Articolo
    # art = Articolo.objects.get(id=10)
    # art.delete()
    # #
    # Articolo.objects.filter(titolo="Il mare").delete()
    # #
    # Articolo.objects.filter(
    #     titolo="Il mare",
    #     testo="Il mare è bello"
    # ).delete()
    # #
    # # Delete di tutti gli oggetti Articolo
    # Articolo.objects.all().delete()
    # #
    # # Update di un oggetto Articolo
    # art = Articolo.objects.get(id=5)  # recuperi l’oggetto
    # art.titolo = "Nuovo titolo"  # modifichi i campi
    # art.testo = "Testo aggiornato"
    # art.save()  # salvi nel database
    # #
    # Articolo.objects.filter(id=5).update(
    #    titolo="Nuovo titolo",
    #    testo="Testo aggiornato"
    # )
    # #
    # Articolo.objects.filter(
    #     titolo="Il mare",
    #     giornalista_id=3
    # ).update(titolo="Mare calmo")
    #
    # # Select di un oggetto Articolo
    # art = Articolo.objects.get(id=5)
    # #
    # art = Articolo.objects.get(titolo="Il mare")
    # #
    # art = Articolo.objects.filter(titolo="Il mare").first()
    # #
    # art = Articolo.objects.get(
    #     titolo="Il mare",
    #     giornalista_id=3
    # )
    # #
    #
    articolo = []
    giornalista = []
    #
    # Estrazione dei dati dal database e
    # definizione di due liste di stinghe
    # for a in Articolo.objects.all():
    #     articolo.append(f"{a.titolo}, {a.testo}")
    #
    if Giornalista.objects.exists():
        for g in Giornalista.objects.all():
            giornalista.append(f"{g.nome} {g.cognome}")
    #
    #response = ', '.join(articolo) + "<br>" + ', '.join(giornalista)
    #
    if Articolo.objects.exists():
        for a in Articolo.objects.all():
            articolo.append(f"{a.titolo} {a.testo}")
    #
    #response = ', '.join(articolo) + "<br>" + ', '.join(giornalista)
    #
    # Estrazione dei dati dal database e
    # definizione di due queryset
    articolo = Articolo.objects.all()
    giornalista = Giornalista.objects.all()

    #return HttpResponse(f"<h1> Home </h1> <p>{response}</p>")
    context = {"articolo": articolo, "giornalista": giornalista}
    return render(request, "news/home.html", context)

def about_us(request):
    return HttpResponse("Pagina di presentazione")