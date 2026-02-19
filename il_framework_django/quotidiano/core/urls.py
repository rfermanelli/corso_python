"""
URL configuration for quotidiano project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Importazione della funzione di routing:
from django.urls import path

# Importazione delle funzioni controller:
from core.views import articolo, dettaglio_articolo

urlpatterns = [
    # Definizione di un percorso di routing contenente un valore dinamico intero:
    path('articolo/<int:primary_key>', articolo),
    path('dettaglio_articolo/', dettaglio_articolo)
]