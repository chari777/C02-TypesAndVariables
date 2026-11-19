###
# Odczytuje plik linia po linii i wypisuje kraje z numerami
#
# enumerate() zwraca parę (numer, wartość) dla każdej linii.
# start=1 sprawia, że numeracja zaczyna się od 1 (domyślnie od 0).
with open('countries.txt', 'r', encoding='utf-8') as file:
    for number, line in enumerate(file, start=1):
        # end="" - linia z pliku już ma znak nowej linii '\n' na końcu,
        # więc nie chcemy dodawać kolejnego.
        print(f'{number}. {line}', end="")
