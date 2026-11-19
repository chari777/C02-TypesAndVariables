# KROKI:
# 1. Użytkownik podaje imię, np. 'Ania'.
# 2. for char in name: bierzemy każdą literę po kolei.
# 3. icao(char) zwraca słowo: 'A' -> 'Alfa', 'N' -> 'November'.
# 4. end=' ' - słowa wypisują się w jednej linii, oddzielone spacją.
###
# Zamienia literę na odpowiadające jej słowo z alfabetu ICAO
#
# Funkcja zwraca słowo dla danej litery.
def icao(letter):
    # capitalize() zamienia pierwszą literę na wielką, np. 'a' -> 'A'.
    # Dzięki temu nie musimy sprawdzać małych liter osobno.
    letter = letter.capitalize()
    if letter == 'A':
        icao_name = 'Alfa'
    elif letter == 'B':
        icao_name = 'Bravo'
    elif letter == 'C':
        icao_name = 'Charlie'
    elif letter == 'D':
        icao_name = 'Delta'
    elif letter == 'E':
        icao_name = 'Echo'
    elif letter == 'F':
        icao_name = 'Foxtrot'
    elif letter == 'G':
        icao_name = 'Golf'
    elif letter == 'H':
        icao_name = 'Hotel'
    elif letter == 'I':
        icao_name = 'India'
    elif letter == 'J':
        icao_name = 'Juliett'
    elif letter == 'K':
        icao_name = 'Kilo'
    elif letter == 'L':
        icao_name = 'Lima'
    elif letter == 'M':
        icao_name = 'Mike'
    elif letter == 'N':
        icao_name = 'November'
    elif letter == 'O':
        icao_name = 'Oscar'
    elif letter == 'P':
        icao_name = 'Papa'
    elif letter == 'Q':
        icao_name = 'Quebec'
    elif letter == 'R':
        icao_name = 'Romeo'
    elif letter == 'S':
        icao_name = 'Sierra'
    elif letter == 'T':
        icao_name = 'Tango'
    elif letter == 'U':
        icao_name = 'Uniform'
    elif letter == 'V':
        icao_name = 'Victor'
    elif letter == 'W':
        icao_name = 'Whiskey'
    elif letter == 'X':
        icao_name = 'X-ray'
    elif letter == 'Y':
        icao_name = 'Yankee'
    elif letter == 'Z':
        icao_name = 'Zulu'
    else:
        # Znaki spoza alfabetu (cyfry, spacje, znaki specjalne) dostają '???'
        icao_name = '???'

    return icao_name

# Program główny: wczytujemy imię i literujemy je alfabetem ICAO
name = input('Enter your name: ')
print('ICAO words for spelling out your name:')

# Pętla for bierze po kolei każdy znak z imienia
for char in name:
    word = icao(char)
    # end=' ' sprawia, że kolejne słowa wypisują się obok siebie, po spacji
    print(word, end=' ')
# Pusty print() przechodzi do nowej linii po wypisaniu wszystkich słów
print()
