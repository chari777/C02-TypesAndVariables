###
# Funkcja zwracająca pełną nazwę dnia tygodnia na podstawie jego numeru
#
# Zamiast długiego łańcucha if/elif używamy listy.
# Indeks listy zaczyna się od 0, a dni są numerowane od 1,
# dlatego od numeru dnia odejmujemy 1.
def day_name(day_number):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']
    # Zabezpieczenie: jeśli numer jest poza zakresem 1..7, nie wyświetlamy
    # błędu indeksu, tylko czytelny komunikat.
    if 1 <= day_number <= 7:
        return weekdays[day_number - 1]
    return 'Invalid day number'

# Wywołania funkcji dla przykładowych numerów
print('The name of day 5 in the week is', day_name(5))
print('The name of day 3 in the week is', day_name(3))
print('The name of day 7 in the week is', day_name(7))
