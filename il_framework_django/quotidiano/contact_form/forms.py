# Importazione del modulo forms:
from django import forms

# Definizione della classe di controllo del form:
class ContactForm(forms.Form):
    nome = forms.CharField(max_length=100)
    cognome = forms.CharField()
    email = forms.EmailField()
    telefono = forms.CharField()
    testo = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "Scrivi qui il tuo messaggio: "}
        )
    )









