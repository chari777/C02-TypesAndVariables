###
# Wypisuje informacje o komputerze z pliku computer.json
#
import json

# encoding='utf-8' - plik może zawierać polskie znaki
with open('computer.json', 'r', encoding='utf-8') as file:
    # json.load() zamienia zawartość pliku na słownik Pythona
    data = json.load(file)

print('COMPUTER INFORMATION')
print('====================')
# items() daje pary (klucz, wartość), które wypisujemy jedna pod drugą
for key, value in data.items():
    print(f'{key}: {value}')
