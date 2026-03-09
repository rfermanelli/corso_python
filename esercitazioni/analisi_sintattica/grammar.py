TERMINALI_LSW = ["il", "un", "ha", "padawan", "maestro"]

NON_TERMINALI_LSW = ["ARTICOLO", "SOSTANTIVO", "VERBO", "SOGGETTO", "OGGETTO", "GRUPPO_VERBALE", "FRASE"]

produzioni_lsw = {
    "ARTICOLO": ["il", "un"],
    "SOSTANTIVO": ["padawan", "maestro"],
    "VERBO": ["ha"],
    "SOGGETTO": ["ARTICOLO", "SOSTANTIVO"],
    "OGGETTO": ["ARTICOLO", "SOSTANTIVO"],
    "GRUPPO_VERBALE": ["ha", "OGGETTO"],
    "FRASE": ["SOGGETTO", "GRUPPO_VERBALE"]
}
