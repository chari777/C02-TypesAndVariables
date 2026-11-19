# KROKI RECURSJI (na przykładzie silni 5!):
# factorial(5) = 5 * factorial(4)
#   factorial(4) = 4 * factorial(3)
#     factorial(3) = 3 * factorial(2)
#       factorial(2) = 2 * factorial(1)
#         factorial(1) = 1   <- PRZYPADEK BAZOWY, koniec wywołań
# Potem wyniki wracają w górę: 1 -> 2 -> 6 -> 24 -> 120.
###
# Funkcje rekurencyjne - funkcja, która wywołuje samą siebie.
#
# Każda funkcja rekurencyjna musi mieć:
#   1) warunek zakończenia (przypadek bazowy) - bez niego funkcja wywoływałaby się w nieskończoność
#   2) wywołanie siebie dla mniejszego problemu

# Silnia: n! = n * (n-1) * ... * 1, przy czym 0! = 1
def factorial(n):
    # Przypadek bazowy: 0! i 1! są równe 1, tu kończymy rekurencję
    if n == 0 or n == 1:
        return 1
    # n! = n * (n-1)!  - wywołujemy siebie dla mniejszej liczby
    return n * factorial(n - 1)

# Suma liczb naturalnych od 1 do n: 1 + 2 + ... + n
def sum_natural(n):
    # Przypadek bazowy: suma od 1 do 1 to 1 (a dla 0 też przyjmujemy 0)
    if n <= 1:
        return n
    # Suma do n = n + suma do (n-1)
    return n + sum_natural(n - 1)

# Potęga x^n, z użyciem rekurencji: x^n = x * x^(n-1)
def power(x, n):
    # Każda potęga z zerowym wykładnikiem daje 1
    if n == 0:
        return 1
    return x * power(x, n - 1)

# Program główny - wywołania funkcji i wypisanie wyników
if __name__ == "__main__":
    print('Factorial of 5 is', factorial(5))
    print('Sum of natural numbers from 1 to 10 is', sum_natural(10))
    print('5 to the power of 3 is', power(5, 3))
