# KROKI:
# 1. Pobieramy trzy boki a, b, c (float, bo mogą mieć część ułamkową).
# 2. Obliczamy połowę obwodu: p = (a + b + c) / 2.
# 3. Wzór Herona: pole = pierwiastek z p*(p-a)*(p-b)*(p-c).
# 4. math.sqrt() liczy pierwiastek. Format :g pokazuje 6.0 jako 6.
###
# Oblicza pole trójkąta na podstawie długości jego boków
# (wzór Herona)
#
import math

# Funkcja liczy pole trójkąta o bokach a, b, c.
# Wzór Herona: najpierw liczymy połowę obwodu p,
# potem pole = sqrt(p * (p-a) * (p-b) * (p-c))
def triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

# Wariant z klawiatury: użytkownik podaje boki.
# float() zamienia tekst z klawiatury na liczbę rzeczywistą (z przecinkiem).
side_a = float(input('Enter side a: '))
side_b = float(input('Enter side b: '))
side_c = float(input('Enter side c: '))
area_from_keyboard = triangle_area(side_a, side_b, side_c)
print(f'The area of a triangle with sides {side_a}, {side_b}, {side_c} is {area_from_keyboard:g}')

# Trzy przykłady podane w zadaniu.
# Format :g wypisuje 6.0 jako 6, dzięki czemu wynik wygląda tak jak w zadaniu.
print(f'The area of a triangle with sides 3, 4, 5 is {triangle_area(3, 4, 5):g}')
print(f'The area of a triangle with sides 5, 12, 13 is {triangle_area(5, 12, 13):g}')
print(f'The area of a triangle with sides 7, 24, 25 is {triangle_area(7, 24, 25):g}')
