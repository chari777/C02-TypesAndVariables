###
# Średnie ceny pokoi w hotelach w Krakowie i w Sopocie
#
hotels_in_Krakow = [
    {"name": "Sky", "price": 320.00},
    {"name": "Metropol", "price": 480.00},
    {"name": "New Port", "price": 420.00},
    {"name": "Aparthotel", "price": 390.00}
]

hotels_in_Sopot = [
    {"name": "Focus", "price": 510.00},
    {"name": "Aqua", "price": 345.00},
    {"name": "La Boutique", "price": 390.00},
    {"name": "Marina", "price": 410.00}
]

# Zwraca listę nazw hoteli oddzielonych przecinkiem
def hotel_list(hotels):
    names = []
    for hotel in hotels:
        names.append(hotel["name"])
    return ",".join(names)

# Zwraca średnią cenę pokoju, zaokrągloną do liczby całkowitej.
# Zaokrąglamy "po szkolnemu" (połówki w górę): floor(x + 0.5).
# Wbudowane round() zaokrągla połówki do parzystej (402.5 -> 402), co nie pasuje do szkolnej zasady.
def avg_price(hotels):
    import math
    total = 0
    for hotel in hotels:
        total += hotel["price"]
    average = total / len(hotels)
    return math.floor(average + 0.5)

krakow_avg = avg_price(hotels_in_Krakow)
sopot_avg = avg_price(hotels_in_Sopot)

print(f'Hotels in Krakow: {hotel_list(hotels_in_Krakow)}')
print(f'Average hotel price in Krakow: {krakow_avg}')
print(f'Hotels in Sopot: {hotel_list(hotels_in_Sopot)}')
print(f'Average hotel price in Sopot: {sopot_avg}')

# Tańsze miasto to to, którego średnia cena jest niższa
if krakow_avg < sopot_avg:
    print('Cheaper hotels in: Krakow')
elif sopot_avg < krakow_avg:
    print('Cheaper hotels in: Sopot')
else:
    print('Cheaper hotels in: both cities cost the same')
