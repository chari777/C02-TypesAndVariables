###
# Wypisuje dane psów młodszych niż 5 lat z pliku dogs.json
#
import json

with open('dogs.json', 'r', encoding='utf-8') as file:
    dogs = json.load(file)

for dog in dogs:
    # Warunek: wiek mniejszy niż 5 lat
    if dog['age'] < 5:
        for key, value in dog.items():
            print(f'{key}: {value}')
        print()
