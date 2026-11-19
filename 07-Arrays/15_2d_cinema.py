# KROKI:
# Macierz to lista list: cinema_seats[wiersz][miejsce].
# Ludzie liczą od 1, Python od 0 - dlatego w seat_status odejmujemy 1.
# Liczenie wolnych miejsc: podwójna pętla for (wiersz, a w nim miejsce).
###
# Plan miejsc w kinie 5x5. A = wolne (Available), B = zajęte (Booked)
#
cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]

# Liczba wszystkich miejsc: liczba wierszy razy liczba miejsc w wierszu
def seats_total(seats):
    return len(seats) * len(seats[0])

# Liczymy pola z literą 'A'
def seats_available(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == 'A':
                count += 1
    return count

# Liczymy pola z literą 'B'
def seats_booked(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == 'B':
                count += 1
    return count

# Status miejsca w podanym wierszu i miejscu.
# Ludzie liczą od 1, a indeksy listy zaczynają się od 0, więc odejmujemy 1.
def seat_status(seats, row, place):
    if seats[row - 1][place - 1] == 'A':
        return 'available'
    return 'booked'

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))
