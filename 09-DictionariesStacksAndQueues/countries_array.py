###
# Tablica (lista) z pięcioma słownikami: kraj i jego liczba ludności
#
countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83000000},
    {"name": "France", "population": 67000000},
    {"name": "Italy", "population": 59000000},
    {"name": "Spain", "population": 47000000}
]

print(f"{'COUNTRY':<10}{'POPULATION':>12}")
# Każdy element listy to słownik, więc odwołujemy się do jego pól po kluczach
for country in countries:
    # :<10 - napis wyrównany do lewej na 10 znaków, :>12 - liczba do prawej na 12
    print(f"{country['name']:<10}{country['population']:>12}")
