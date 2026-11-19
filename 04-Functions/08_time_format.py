# KROKI:
# Format 24h: godziny i minuty z zerem z przodu -> f'{h:02d}:{m:02d}'.
# Format 12h:
#   1. Godzina < 12 -> 'am', inaczej 'pm'.
#   2. hours % 12 daje godzinę w zegarze 12h (15 % 12 = 3, 12 % 12 = 0).
#   3. Jeśli wynik to 0 (północ lub południe), zamieniamy na 12.
#   4. Minuty zawsze z zerem (7:02pm), godzina bez zera (7:30am).
# Testy na końcu: assert sprawdza każdy przykład z zadania.
###
# Funkcja time_string zwraca godzinę jako napis w formacie 24h lub 12h
#
def time_string(hours, minutes, time_format):
    if time_format == '24':
        # f-string: {liczba:02d} wypełnia zerem z lewej do 2 cyfr,
        # więc 8 zamienia się w 08, a 5 w 05.
        return f'{hours:02d}:{minutes:02d}'

    if time_format == '12':
        # Przed południem (0-11) -> 'am', po południu (12-23) -> 'pm'
        if hours < 12:
            suffix = 'am'
        else:
            suffix = 'pm'
        # Zamiana na format 12h: reszta z dzielenia przez 12.
        # 0 oznacza północ, więc wtedy zamieniamy na 12.
        hour12 = hours % 12
        if hour12 == 0:
            hour12 = 12
        # W formacie 12h godzina NIE ma zera z przodu (7:30am, nie 07:30am)
        return f'{hour12}:{minutes:02d}{suffix}'

    # Nieznany format - zwracamy pusty napis
    return ''

# Testy - sprawdzamy, czy funkcja zwraca dokładnie to, co jest w zadaniu.
# assert zatrzymuje program, jeśli warunek jest fałszywy.
tests = [
    (time_string(15, 38, '24'), '15:38'),
    (time_string(8, 3, '24'), '08:03'),
    (time_string(0, 5, '24'), '00:05'),
    (time_string(11, 15, '12'), '11:15am'),
    (time_string(0, 7, '12'), '12:07am'),
    (time_string(7, 30, '12'), '7:30am'),
    (time_string(12, 46, '12'), '12:46pm'),
    (time_string(13, 10, '12'), '1:10pm'),
    (time_string(19, 2, '12'), '7:02pm'),  # w zadaniu '02' - w Pythonie 3 zapis 02 nie jest dozwolony
]
for result, expected in tests:
    print(f'{result:>8}  (expected {expected})  {"OK" if result == expected else "BŁĄD"}')
    assert result == expected
print('All time_string tests passed.')
