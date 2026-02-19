# Interi
print("Gli interi:")
print("La conversione intera dell'intero 1 è:", int(1))
print("La conversione intera della stringa '1' è:", int('1'))
print("La conversione intera del reale 0.1 è:", int(.1))
#print("La conversione intera del complesso 0.1j è:", int(.1j))
print("La conversione della stringa '100' in base ottale è:", int("100", 8))
print()

# Reali
print("I reali:")
print("La conversione reale dell'intero 1 è:", float(1))
print("La conversione reale del reale 1.0 è:", float(1.0))
#print("La conversione reale del complesso 1.0j è:", float(1.0j))
print("La velocità della luce nel vuoto è:", float(3e8), "di metri al secondo")
#print("La conversione del numero in base ottale 100 è:", float('100', 8))
# La funzione round()
print("la differenza tra i valori 41.8 e 41 senza la funzione round() è:", 418 / 10 - 418 // 10)
print("la differenza tra i valori 41.8 e 41 con la funzione round() è:", round(418 / 10 - 418 // 10, 10))
print()

# I complessi:
print("La conversione complessa dell'intero 1 è:", complex(1))
print("La conversione complessa del reale 1.0 è:", complex(1.0))
print("La conversione complessa del complesso 1 + 1.0j è:", complex(1 + 1.0j))
print("La conversione complessa del complesso 1 + 1.0 è:", complex(1, 1.0))
print("La conversione complessa della stringa '3+7j' è:", complex('3+7j'))
#print("La conversione del numero in base ottale 100 è:", complex('100', 8))
