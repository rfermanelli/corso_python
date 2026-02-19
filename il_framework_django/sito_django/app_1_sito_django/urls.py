from django.urls import path

from app_1_sito_django.views import homepage, chi_siamo

urlpatterns = [
    path('home/', homepage),
    path('chi-siamo/', chi_siamo)
]