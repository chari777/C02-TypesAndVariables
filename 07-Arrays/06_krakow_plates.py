###
# Wypisuje numery rejestracyjne samochodów z Krakowa.
# Numery z Krakowa zaczynają się od liter 'KR' lub 'KK'.
#
polish_license_plates = [
    'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
    'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
    'KK54985', 'LU4864U'
]

counter = 1
for car_number in polish_license_plates:
    # car_number[:2] to pierwsze dwa znaki numeru.
    # Sprawdzamy, czy należą do zbioru ('KR', 'KK').
    if car_number[:2] in ('KR', 'KK'):
        print(counter, car_number)
        counter += 1
