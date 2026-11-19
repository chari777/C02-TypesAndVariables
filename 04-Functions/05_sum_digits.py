# KROKI (co dokładnie dzieje się w programie):
# 1. Użytkownik podaje liczbę -> input() zwraca napis, int() zamienia go na liczbę.
# 2. sum_digits(): abs() usuwa minus (-9123 i 9123 mają tę samą sumę cyfr).
# 3. str() zamienia liczbę na napis '9123' - dzięki temu można przejść po znakach.
# 4. Pętla for: każdy znak '9','1','2','3' zamieniamy z powrotem na int i dodajemy do sumy.
# 5. Zwracamy sumę i wypisujemy ją.
###
# Oblicza sumę cyfr liczby całkowitej
#

# Funkcja zwraca sumę cyfr podanej liczby.
def sum_digits(number):
    # abs() usuwa znak minus, żeby liczby ujemne działały tak samo jak dodatnie
    number = abs(number)
    # str() zamienia liczbę na napis, żeby można było przejść po kolejnych cyfrach
    digits_text = str(number)
    total = 0
    for char in digits_text:
        # Każdy znak to pojedyncza cyfra, ale jako napis.
        # int() zamienia go z powrotem na liczbę, którą można dodać.
        total = total + int(char)
    return total

# Wczytanie liczby z klawiatury. int() zamienia napis na liczbę całkowitą.
any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')
