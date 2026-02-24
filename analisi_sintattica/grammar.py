lessico = ["il", "un", "ha", "padawan", "maestro"]

categorie_sintattiche = ["ARTICOLO", "SOSTANTIVO", "VERBO", "SOGGETTO", "OGGETTO", "GRUPPO_VERBALE", "FRASE"]

produzioni_sintattiche = {
    "ARTICOLO": ["il", "un"],
    "SOSTANTIVO": ["padawan", "maestro"],
    "VERBO": ["ha"],
    "SOGGETTO": ["ARTICOLO", "SOSTANTIVO"],
    "OGGETTO": ["ARTICOLO", "SOSTANTIVO"],
    "GRUPPO_VERBALE": ["ha", "OGGETTO"],
    "FRASE": ["SOGGETTO", "GRUPPO_VERBALE"]
}
