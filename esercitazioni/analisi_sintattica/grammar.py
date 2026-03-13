from dataclasses import dataclass, field

@dataclass
class TerminalsLsw:
    terminals: list[str] = ("IL", "UN", "HA", "MAESTRO", "PADAWAN")


@dataclass
class NonTerminalsLsw:
    non_terminals: list[str] = ("<ARTICOLO>", "<SOSTANTIVO>", "<SOGGETTO>", "<OGGETTO>", "<VERBO>", "<GRUPPO_VERBALE>", "<FRASE>")


@dataclass
class Productions:
    syntax: dict[str, list[str]] = field(default_factory=lambda: {
        "articolo": ["IL", "UN"],
        "sostantivo": ["MAESTRO", "PADAWAN"],
        "verbo": ["HA"],
        "soggetto": ["ARTICOLO", "SOSTANTIVO"],
        "oggetto": ["ARTICOLO", "SOSTANTIVO"],
        "gruppo_verbale": ["VERBO", "OGGETTO"],
        "frase": ["SOGGETTO", "GRUPPO_VERBALE"]
    })
