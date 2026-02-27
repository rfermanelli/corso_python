from django.db import models

# Create your models here.
from django.db import models

# =====================================================
# STRUTTURA ORGANIZZATIVA
# =====================================================

class Dipartimento(models.Model):
    nome = models.CharField(max_length=100)
    sede = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class CorsoDiLaurea(models.Model):
    nome = models.CharField(max_length=150)
    classe_laurea = models.CharField(max_length=20)
    tipo = models.CharField(max_length=10)
    dipartimento = models.ForeignKey(Dipartimento, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome


class Docente(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    ruolo = models.CharField(max_length=50)
    dipartimento = models.ForeignKey(Dipartimento, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.nome} {self.cognome}"


# =====================================================
# OFFERTA FORMATIVA
# =====================================================

class SSD(models.Model):
    codice_ssd = models.CharField(max_length=20, primary_key=True)
    descrizione = models.CharField(max_length=150)


class Corso(models.Model):
    nome = models.CharField(max_length=150)
    cfu = models.PositiveIntegerField()
    ssd = models.ForeignKey(SSD, on_delete=models.RESTRICT)
    anno_di_corso = models.PositiveIntegerField()
    semestre = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class AnnoAccademico(models.Model):
    anno_inizio = models.IntegerField()
    anno_fine = models.IntegerField()
    stato = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.anno_inizio}/{self.anno_fine}"


class OffertaFormativa(models.Model):
    corso_di_laurea = models.ForeignKey(CorsoDiLaurea, on_delete=models.CASCADE)
    corso = models.ForeignKey(Corso, on_delete=models.CASCADE)
    anno_accademico = models.ForeignKey(AnnoAccademico, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("corso_di_laurea", "corso")


class Docenza(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    corso = models.ForeignKey(Corso, on_delete=models.CASCADE)
    anno_accademico = models.ForeignKey(AnnoAccademico, on_delete=models.CASCADE)
    titolare = models.BooleanField()

    class Meta:
        unique_together = ("docente", "corso", "anno_accademico")


class Propedeuticita(models.Model):
    corso = models.ForeignKey(
        Corso,
        on_delete=models.CASCADE,
        related_name="corso_principale"
    )
    corso_propedeutico = models.ForeignKey(
        Corso,
        on_delete=models.CASCADE,
        related_name="corso_prerequisito"
    )

    class Meta:
        unique_together = ("corso", "corso_propedeutico")


# =====================================================
# CARRIERA STUDENTE
# =====================================================

class Studente(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    data_nascita = models.DateField()
    email = models.EmailField(unique=True)
    corso_di_laurea = models.ForeignKey(CorsoDiLaurea, on_delete=models.RESTRICT)


class StatoIscrizione(models.Model):
    descrizione = models.CharField(max_length=30, unique=True)


class IscrizioneAnnuale(models.Model):
    studente = models.ForeignKey(Studente, on_delete=models.CASCADE)
    anno_accademico = models.ForeignKey(AnnoAccademico, on_delete=models.CASCADE)
    stato = models.ForeignKey(StatoIscrizione, on_delete=models.RESTRICT)
    data_immatricolazione = models.DateField()

    class Meta:
        unique_together = ("studente", "anno_accademico")


class PianoDiStudi(models.Model):
    studente = models.ForeignKey(Studente, on_delete=models.CASCADE)
    anno_accademico = models.ForeignKey(AnnoAccademico, on_delete=models.CASCADE)
    stato_approvazione = models.CharField(max_length=30)
    data_presentazione = models.DateField()


class PianoDiStudiDettaglio(models.Model):
    piano = models.ForeignKey(PianoDiStudi, on_delete=models.CASCADE)
    corso = models.ForeignKey(Corso, on_delete=models.CASCADE)
    tipologia = models.CharField(max_length=20)

    class Meta:
        unique_together = ("piano", "corso")


# =====================================================
# ORGANIZZAZIONE ESAMI
# =====================================================

class TipoSessione(models.Model):
    descrizione = models.CharField(max_length=30, unique=True)


class SessioneEsami(models.Model):
    tipo = models.ForeignKey(TipoSessione, on_delete=models.RESTRICT)
    data_inizio = models.DateField()
    data_fine = models.DateField()
    anno_accademico = models.ForeignKey(AnnoAccademico, on_delete=models.CASCADE)


class AppelloEsame(models.Model):
    data_appello = models.DateField()
    aula = models.CharField(max_length=50, blank=True, null=True)
    modalita = models.CharField(max_length=20)
    corso = models.ForeignKey(Corso, on_delete=models.CASCADE)
    sessione = models.ForeignKey(SessioneEsami, on_delete=models.CASCADE)


class CommissioneEsame(models.Model):
    appello = models.OneToOneField(AppelloEsame, on_delete=models.CASCADE)
    presidente = models.ForeignKey(Docente, on_delete=models.RESTRICT)


class CommissioneComponente(models.Model):
    commissione = models.ForeignKey(CommissioneEsame, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    ruolo = models.CharField(max_length=50)

    class Meta:
        unique_together = ("commissione", "docente")


# =====================================================
# GESTIONE ESAMI
# =====================================================

class StatoPrenotazione(models.Model):
    descrizione = models.CharField(max_length=30, unique=True)


class PrenotazioneEsame(models.Model):
    studente = models.ForeignKey(Studente, on_delete=models.CASCADE)
    appello = models.ForeignKey(AppelloEsame, on_delete=models.CASCADE)
    data_prenotazione = models.DateField()
    stato = models.ForeignKey(StatoPrenotazione, on_delete=models.RESTRICT)

    class Meta:
        unique_together = ("studente", "appello")


class StatoEsame(models.Model):
    descrizione = models.CharField(max_length=30, unique=True)


class VerbaleEsame(models.Model):
    appello = models.OneToOneField(AppelloEsame, on_delete=models.CASCADE)
    data_chiusura = models.DateField(blank=True, null=True)
    firma_digitale = models.BooleanField(default=False)


class EsameSostenuto(models.Model):
    studente = models.ForeignKey(Studente, on_delete=models.CASCADE)
    appello = models.ForeignKey(AppelloEsame, on_delete=models.CASCADE)
    voto = models.IntegerField(blank=True, null=True)
    lode = models.BooleanField(default=False)
    stato = models.ForeignKey(StatoEsame, on_delete=models.RESTRICT)
    data_registrazione = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ("studente", "appello")


