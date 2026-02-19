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

# Importazione della funzione di amministrazione:
from django.contrib import admin

# Importazione delle funzioni di routing:
from django.urls import path, include

# Importazione delle funzioni controller:
from news.views import home, about_us
from core.views import articolo
from contact_form.views import contact_form

# Definizione dei percorsi che mappano gli indirizzi con le funzioni controller:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="Pagina di home"),
    path('about/', about_us, name="Pagina di presentazione"),
    #
    path('core/', include('core.urls')),
    path('contact_form/', include('contact_form.urls'))
]
