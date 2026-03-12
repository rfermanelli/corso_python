nome = "Luca"
livello = 8
hp = 73
hp_max = 100
mana = 42

dashboard = f"""
🧙 Personaggio: {nome}
⭐ Livello: {livello}
❤️ HP: {hp}/{hp_max} ({hp / hp_max:.0%})
🔮 Mana: {mana}
⚔️ Stato: {"PRONTO" if hp > 50 else "IN PERICOLO"}
"""

print(dashboard)
