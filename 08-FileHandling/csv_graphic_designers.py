###
# Wypisuje imię, nazwisko i email grafików z pliku it_company.csv
# Moduł csv poprawnie czyta pliki CSV (np. gdy pola zawierają przecinki w cudzysłowach).
#
import csv

print('GRAPHIC DESIGNERS')
print('=================')

with open('it_company.csv', 'r', encoding='utf-8', newline='') as file:
    # DictReader zamienia każdy wiersz na słownik: nazwa kolumny -> wartość
    reader = csv.DictReader(file)
    for row in reader:
        if row['Job Title'] == 'Graphic Designer':
            print(f"{row['First Name']} {row['Last Name']},{row['Email']}")
