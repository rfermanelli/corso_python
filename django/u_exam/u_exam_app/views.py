from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import *

import json


# ==========================================================
# UTILITÀ GENERICA
# ==========================================================

def parse_body(request):
    try:
        return json.loads(request.body.decode("utf-8"))
    except Exception:
        return {}


# ==========================================================
# CRUD GENERICO BASE (RIUTILIZZABILE)
# ==========================================================

class BaseCRUDView(View):
    model = None
    fields = []

    def get(self, request, pk=None):
        if pk:
            obj = get_object_or_404(self.model, pk=pk)
            return JsonResponse(self.serialize(obj))

        objects = self.model.objects.all()
        return JsonResponse(
            [self.serialize(obj) for obj in objects],
            safe=False
        )

    def post(self, request):
        data = parse_body(request)
        obj = self.model.objects.create(**data)
        return JsonResponse(self.serialize(obj))

    def put(self, request, pk):
        data = parse_body(request)
        obj = get_object_or_404(self.model, pk=pk)

        for field in self.fields:
            if field in data:
                setattr(obj, field, data[field])

        obj.save()
        return JsonResponse(self.serialize(obj))

    def delete(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        obj.delete()
        return JsonResponse({"status": "deleted"})

    def serialize(self, obj):
        result = {}
        for field in obj._meta.fields:
            result[field.name] = getattr(obj, field.name)
        return result


# ==========================================================
# VIEWS PER OGNI MODEL
# ==========================================================

class DipartimentoView(BaseCRUDView):
    model = Dipartimento
    fields = ["nome", "sede"]


class CorsoDiLaureaView(BaseCRUDView):
    model = CorsoDiLaurea
    fields = ["nome", "classe_laurea", "tipo", "dipartimento_id"]


class DocenteView(BaseCRUDView):
    model = Docente
    fields = ["nome", "cognome", "email", "ruolo", "dipartimento_id"]


class SSDView(BaseCRUDView):
    model = SSD
    fields = ["codice_ssd", "descrizione"]


class CorsoView(BaseCRUDView):
    model = Corso
    fields = ["nome", "cfu", "ssd_id", "anno_di_corso", "semestre"]


class AnnoAccademicoView(BaseCRUDView):
    model = AnnoAccademico
    fields = ["anno_inizio", "anno_fine", "stato"]


class OffertaFormativaView(BaseCRUDView):
    model = OffertaFormativa
    fields = ["corso_di_laurea_id", "corso_id", "anno_accademico_id"]


class DocenzaView(BaseCRUDView):
    model = Docenza
    fields = ["docente_id", "corso_id", "anno_accademico_id", "titolare"]


class PropedeuticitaView(BaseCRUDView):
    model = Propedeuticita
    fields = ["corso_id", "corso_propedeutico_id"]


class StudenteView(BaseCRUDView):
    model = Studente
    fields = ["nome", "cognome", "data_nascita", "email", "corso_di_laurea_id"]


class StatoIscrizioneView(BaseCRUDView):
    model = StatoIscrizione
    fields = ["descrizione"]


class IscrizioneAnnualeView(BaseCRUDView):
    model = IscrizioneAnnuale
    fields = ["studente_id", "anno_accademico_id", "stato_id", "data_immatricolazione"]


class PianoDiStudiView(BaseCRUDView):
    model = PianoDiStudi
    fields = ["studente_id", "anno_accademico_id", "stato_approvazione", "data_presentazione"]


class PianoDiStudiDettaglioView(BaseCRUDView):
    model = PianoDiStudiDettaglio
    fields = ["piano_id", "corso_id", "tipologia"]


class TipoSessioneView(BaseCRUDView):
    model = TipoSessione
    fields = ["descrizione"]


class SessioneEsamiView(BaseCRUDView):
    model = SessioneEsami
    fields = ["tipo_id", "data_inizio", "data_fine", "anno_accademico_id"]


class AppelloEsameView(BaseCRUDView):
    model = AppelloEsame
    fields = ["data_appello", "aula", "modalita", "corso_id", "sessione_id"]


class CommissioneEsameView(BaseCRUDView):
    model = CommissioneEsame
    fields = ["appello_id", "presidente_id"]


class CommissioneComponenteView(BaseCRUDView):
    model = CommissioneComponente
    fields = ["commissione_id", "docente_id", "ruolo"]


class StatoPrenotazioneView(BaseCRUDView):
    model = StatoPrenotazione
    fields = ["descrizione"]


class PrenotazioneEsameView(BaseCRUDView):
    model = PrenotazioneEsame
    fields = ["studente_id", "appello_id", "data_prenotazione", "stato_id"]


class StatoEsameView(BaseCRUDView):
    model = StatoEsame
    fields = ["descrizione"]


class VerbaleEsameView(BaseCRUDView):
    model = VerbaleEsame
    fields = ["appello_id", "data_chiusura", "firma_digitale"]


class EsameSostenutoView(BaseCRUDView):
    model = EsameSostenuto
    fields = ["studente_id", "appello_id", "voto", "lode", "stato_id", "data_registrazione"]
