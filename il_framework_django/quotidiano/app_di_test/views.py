from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("<h1>Pagina iniziale del mio sito web</h1>")


def about_us(request):
    return HttpResponse("Siamo il gruppo di programmatore informatico")

