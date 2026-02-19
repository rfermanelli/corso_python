nome = "Alex"
livello = 12
xp = 3450
classe = "Mago"

profilo = (
    "👤 Nome: {0}\n"
    "🧙 Classe: {classe}\n"
    "⭐ Livello: {1}\n"
    "⚡ XP: {xp:,}\n"
    "🔥 Stato: {2}"
).format(
    nome,
    livello,
    "PRONTO ALLA BATTAGLIA",
    classe=classe,
    xp=xp
)

print(profilo)
