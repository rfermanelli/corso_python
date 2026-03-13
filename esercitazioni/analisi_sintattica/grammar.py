from dataclasses import dataclass, field

@dataclass(frozen=True)
class TerminalsLsw:
    terminals: list[str] = ("IL", "UN", "HA", "MAESTRO", "PADAWAN")


@dataclass(frozen=True)
class NonTerminalsLsw:
    non_terminals: list[str] = ("<ARTICOLO>", "<SOSTANTIVO>", "<SOGGETTO>", "<OGGETTO>", "<VERBO>", "<GRUPPO_VERBALE>", "<FRASE>")


@dataclass(frozen=True)
class Productions:
    syntax: dict[str, list[str]] = field(default_factory=lambda: {
        "ARTICOLO": ["IL", "UN"],
        "SOSTANTIVO": ["MAESTRO", "PADAWAN"],
        "VERBO": ["HA"],
        "SOGGETTO": ["ARTICOLO", "SOSTANTIVO"],
        "OGGETTO": ["ARTICOLO", "SOSTANTIVO"],
        "GRUPPO_VERBALE": ["VERBO", "OGGETTO"],
        "FRASE": ["SOGGETTO", "GRUPPO_VERBALE"]
    })
