# Importazione delle funzioni di rendering:
from django.http import HttpResponse
from django.shortcuts import render

# Importazione del form ContactForm e del modello corrispondente Contatto:
from contact_form.forms import ContactForm
from contact_form.models import Contatto

# Create your views here.
# Definizione della funzione controller del form ContactForm:
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contatto = Contatto(nome=form.cleaned_data['nome'],cognome=form.cleaned_data['cognome'],
                                telefono=form.cleaned_data['telefono'], email=form.cleaned_data['email'], testo=form.cleaned_data['testo'])
            contatto.save()
            print(form.cleaned_data)
            print(f"testo: {form.cleaned_data['testo']}")
            return HttpResponse("<h1>Grazie per averci contattato</h1>")
    else:
        form = ContactForm()

    context = {"form": form}
    return render(request, 'contact_form.html', context)


