from django.urls import path
from . import views

urlpatterns = [

    # =====================================================
    # STRUTTURA ORGANIZZATIVA
    # =====================================================

    path("dipartimenti/", views.DipartimentoView.as_view()),
    path("dipartimenti/<int:pk>/", views.DipartimentoView.as_view()),

    path("corsi-di-laurea/", views.CorsoDiLaureaView.as_view()),
    path("corsi-di-laurea/<int:pk>/", views.CorsoDiLaureaView.as_view()),

    path("docenti/", views.DocenteView.as_view()),
    path("docenti/<int:pk>/", views.DocenteView.as_view()),

    # =====================================================
    # OFFERTA FORMATIVA
    # =====================================================

    path("ssd/", views.SSDView.as_view()),
    path("ssd/<str:pk>/", views.SSDView.as_view()),

    path("corsi/", views.CorsoView.as_view()),
    path("corsi/<int:pk>/", views.CorsoView.as_view()),

    path("anni-accademici/", views.AnnoAccademicoView.as_view()),
    path("anni-accademici/<int:pk>/", views.AnnoAccademicoView.as_view()),

    path("offerta-formativa/", views.OffertaFormativaView.as_view()),
    path("offerta-formativa/<int:pk>/", views.OffertaFormativaView.as_view()),

    path("docenze/", views.DocenzaView.as_view()),
    path("docenze/<int:pk>/", views.DocenzaView.as_view()),

    path("propedeuticita/", views.PropedeuticitaView.as_view()),
    path("propedeuticita/<int:pk>/", views.PropedeuticitaView.as_view()),

    # =====================================================
    # CARRIERA STUDENTE
    # =====================================================

    path("studenti/", views.StudenteView.as_view()),
    path("studenti/<int:pk>/", views.StudenteView.as_view()),

    path("stati-iscrizione/", views.StatoIscrizioneView.as_view()),
    path("stati-iscrizione/<int:pk>/", views.StatoIscrizioneView.as_view()),

    path("iscrizioni/", views.IscrizioneAnnualeView.as_view()),
    path("iscrizioni/<int:pk>/", views.IscrizioneAnnualeView.as_view()),

    path("piani-di-studio/", views.PianoDiStudiView.as_view()),
    path("piani-di-studio/<int:pk>/", views.PianoDiStudiView.as_view()),

    path("piano-dettaglio/", views.PianoDiStudiDettaglioView.as_view()),
    path("piano-dettaglio/<int:pk>/", views.PianoDiStudiDettaglioView.as_view()),

    # =====================================================
    # ORGANIZZAZIONE ESAMI
    # =====================================================

    path("tipi-sessione/", views.TipoSessioneView.as_view()),
    path("tipi-sessione/<int:pk>/", views.TipoSessioneView.as_view()),

    path("sessioni/", views.SessioneEsamiView.as_view()),
    path("sessioni/<int:pk>/", views.SessioneEsamiView.as_view()),

    path("appelli/", views.AppelloEsameView.as_view()),
    path("appelli/<int:pk>/", views.AppelloEsameView.as_view()),

    path("commissioni/", views.CommissioneEsameView.as_view()),
    path("commissioni/<int:pk>/", views.CommissioneEsameView.as_view()),

    path("commissioni-componenti/", views.CommissioneComponenteView.as_view()),
    path("commissioni-componenti/<int:pk>/", views.CommissioneComponenteView.as_view()),

    # =====================================================
    # GESTIONE ESAMI
    # =====================================================

    path("stati-prenotazione/", views.StatoPrenotazioneView.as_view()),
    path("stati-prenotazione/<int:pk>/", views.StatoPrenotazioneView.as_view()),

    path("prenotazioni/", views.PrenotazioneEsameView.as_view()),
    path("prenotazioni/<int:pk>/", views.PrenotazioneEsameView.as_view()),

    path("stati-esame/", views.StatoEsameView.as_view()),
    path("stati-esame/<int:pk>/", views.StatoEsameView.as_view()),

    path("verbali/", views.VerbaleEsameView.as_view()),
    path("verbali/<int:pk>/", views.VerbaleEsameView.as_view()),

    path("esami-sostenuti/", views.EsameSostenutoView.as_view()),
    path("esami-sostenuti/<int:pk>/", views.EsameSostenutoView.as_view()),
]