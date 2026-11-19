###
# Wypisuje produkty, których cena jest mniejsza niż 60, a stan magazynowy mniejszy niż 40.
#
import csv

with open('clothing.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Zamieniamy tekst z pliku na liczby, żeby można było je porównać
        price = float(row['Price'])
        stock = int(row['Stock_Quantity'])
        if price < 60 and stock < 40:
            print(row)
