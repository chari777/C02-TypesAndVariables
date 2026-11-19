# KROKI:
# 1. Wczytujemy cały plik (encoding utf-8, bo jest znak €).
# 2. Wzorzec r'€\s?(\d+(?:\.\d+)?)' łapie znak € i liczbę za nim.
# 3. findall() zwraca listę samych liczb jako napisy: ['102', '30', '15', '20'].
# 4. Zamieniamy każdy napis na float i sumujemy: 102 + 30 + 15 + 20 = 167.
###
# Oblicza łączną kwotę wydaną na zakupy z pliku report.txt (mail od Ann)
#
import re   # moduł do wyrażeń regularnych

# Plik zawiera polskie/specjalne znaki, np. €, dlatego podajemy kodowanie UTF-8
email_file = 'report.txt'

with open(email_file, 'r', encoding='utf-8') as file:
    email = file.read()

# Wzorzec: znak € i po nim liczba, która może mieć część dziesiętną.
# \d+ - jedna lub więcej cyfr, (?:\.\d+)? - opcjonalnie kropka i cyfry.
# Nawias () wycina samą liczbę, bez znaku €.
pattern = r'€\s?(\d+(?:\.\d+)?)'

# findall() zwraca listę wszystkich dopasowań, czyli napisy z liczbami
amounts = re.findall(pattern, email)

total = 0.0
for amount in amounts:
    # Zamieniamy napis na liczbę zmiennoprzecinkową
    total += float(amount)

print('Amounts found:', amounts)
print(f'Total value of money spent: €{total:.2f}')
