# KROKI:
# 1. load_reservations() - wczytuje plik i zwraca listę rezerwacji (z klucza 'reservations').
# 2. count_paid() - liczy rezerwacje, w których paid == True (lub False).
# 3. total_value() - sumuje nights * price_per_night dla wybranej grupy.
# 4. print_summary() - składa wyniki w czytelny raport.
###
# Podsumowanie rezerwacji hotelowych z pliku reservations.json.
# Program podzielony na funkcje, każda robi jedną rzecz.
#
import json

# Wczytuje listę rezerwacji z pliku
def load_reservations(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # Plik ma strukturę {"reservations": [...]}, więc zwracamy samą listę
    return data['reservations']

# Wartość rezerwacji = liczba nocy * cena za noc
def reservation_value(reservation):
    return reservation['nights'] * reservation['price_per_night']

# Zlicza rezerwacje opłacone lub nieopłacone
def count_paid(reservations, paid):
    count = 0
    for r in reservations:
        if r['paid'] == paid:
            count += 1
    return count

# Sumuje wartość rezerwacji opłaconych lub nieopłaconych
def total_value(reservations, paid):
    total = 0
    for r in reservations:
        if r['paid'] == paid:
            total += reservation_value(r)
    return total

# Wypisuje podsumowanie. Osobna funkcja - łatwiej ją przetestować i zmienić.
def print_summary(reservations):
    print('RESERVATIONS SUMMARY')
    print('====================')
    print('Number of rooms:', len(reservations))
    print('Number of paid reservations:', count_paid(reservations, True))
    print('Number of unpaid reservations:', count_paid(reservations, False))
    print(f'Total value of paid reservations: {total_value(reservations, True):.2f}')
    print(f'Total value of unpaid reservations: {total_value(reservations, False):.2f}')

if __name__ == "__main__":
    reservations = load_reservations('reservations.json')
    print_summary(reservations)
