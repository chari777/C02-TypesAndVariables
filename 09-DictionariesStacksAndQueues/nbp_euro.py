# KROKI:
# 1. urllib.request.urlopen() pobiera dane z adresu API NBP (tekst w formacie JSON).
# 2. json.loads() zamienia tekst na słownik/listę Pythona.
# 3. json.dump() zapisuje dane do euro.json (żeby można je było otworzyć offline).
# 4. Czytamy plik z dysku i wypisujemy tabelę: effectiveDate, bid (kupno), ask (sprzedaż).
# Uwaga: wymaga połączenia z internetem w pierwszym kroku.
###
# Pobiera ostatnie 10 kursów EUR z API NBP, zapisuje do euro.json
# i wyświetla je w tabeli.
#
# API NBP: https://api.nbp.pl/en.html
# Tabela C zawiera kursy kupna (bid) i sprzedaży (ask) walut.
#
import json
import urllib.request

URL = 'https://api.nbp.pl/api/exchangerates/rates/c/eur/last/10/?format=json'
FILE_NAME = 'euro.json'

# 1. Pobieramy dane z internetu. urlopen() otrzymuje odpowiedź serwera.
with urllib.request.urlopen(URL) as response:
    raw = response.read().decode('utf-8')

# 2. Sprawdzamy, czy dane są poprawnym JSON-em, i zapisujemy je do pliku.
data = json.loads(raw)
with open(FILE_NAME, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
print(f'Saved {len(data["rates"])} rates to {FILE_NAME}')

# 3. Wczytujemy plik z dysku i wyświetlamy tabelę (w wersji z pliku, zgodnie z zadaniem)
with open(FILE_NAME, 'r', encoding='utf-8') as file:
    euro_data = json.load(file)

print()
print(f"{'Date':<16}{'Buying Rate':<16}{'Selling Rate':<16}")
print('=' * 48)
for rate in euro_data['rates']:
    # :<16 wyrównuje do lewej na 16 znaków, :.4f pokazuje 4 miejsca po przecinku
    print(f"{rate['effectiveDate']:<16}{rate['bid']:<16.4f}{rate['ask']:<16.4f}")
