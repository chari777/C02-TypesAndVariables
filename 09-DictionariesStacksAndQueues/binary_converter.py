# KROKI na przykładzie 18:
# 18 % 2 = 0 (reszta) -> na stos; 18 // 2 = 9
#  9 % 2 = 1          -> na stos; 9 // 2 = 4
#  4 % 2 = 0          -> na stos; 4 // 2 = 2
#  2 % 2 = 0          -> na stos; 2 // 2 = 1
#  1 % 2 = 1          -> na stos; 1 // 2 = 0 (koniec)
# Zdejmujemy ze stosu (od ostatnio odłożonej): 1,0,0,1,0 -> 10010.
###
# Zamiana liczby naturalnej na system binarny przy użyciu stosu.
# Dzielimy liczbę przez 2, reszty odkładamy na stos, a potem zdejmujemy je w odwrotnej kolejności.
#
import queue

def to_binary(number):
    stack = queue.LifoQueue()
    # Dla liczby 0 pętla nie wykona się wcale, więc obsługujemy ten przypadek osobno
    if number == 0:
        return '0'
    while number > 0:
        # % 2 to reszta z dzielenia przez 2 (0 lub 1) - to kolejna cyfra binarna
        stack.put(number % 2)
        # // to dzielenie całkowite (bez części ułamkowej)
        number = number // 2
    # Zdejmujemy cyfry ze stosu - dostajemy je od najstarszej, czyli od najbardziej znaczącej
    result = ''
    while not stack.empty():
        result += str(stack.get())
    return result

natural_number = int(input('Natural number: '))
print('Binary number:', to_binary(natural_number))
