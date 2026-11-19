# KROKI:
# 1. Z province.csv budujemy słownik: 'K' -> 'Małopolskie', 'W' -> 'Mazowieckie', ...
# 2. Tworzymy licznik {litera: 0} dla każdej litery województwa.
# 3. Dla każdego numeru rejestracyjnego bierzemy pierwszą literę (plate[0])
#    i dodajemy 1 do licznika tej litery.
# 4. Wypisujemy nazwę województwa i liczbę pojazdów.
###
# Zlicza zarejestrowane pojazdy z każdego województwa Polski.
# Pierwsza litera numeru rejestracyjnego określa województwo (plik province.csv).
#
import csv

# Słownik: pierwsza litera -> nazwa województwa
province_names = {}
with open('province.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        province_names[row['Letter']] = row['Name']

# Zliczamy pojazdy: litera -> liczba pojazdów
counts = {letter: 0 for letter in province_names}
with open('vehicle.txt', 'r', encoding='utf-8') as file:
    for line in file:
        plate = line.strip()
        if plate == '':
            continue   # pusta linia - pomijamy
        letter = plate[0]
        # Liczymy tylko litery znane z listy województw
        if letter in counts:
            counts[letter] += 1

for letter, count in counts.items():
    print(f'{province_names[letter]}: {count}')
