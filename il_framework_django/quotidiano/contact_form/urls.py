from django.urls import path
from contact_form.views import contact_form

urlpatterns = [
    path('contatto/', contact_form, name="Pagina di contatto"),
]