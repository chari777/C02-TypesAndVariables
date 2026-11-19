###
# Wypisuje informacje o miastach z pliku cities.json
#
import json

with open('cities.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Plik to lista słowników - jeden słownik na miasto
for city in data:
    for key, value in city.items():
        print(key, ':', value)
    print()
