###
# Moduł z funkcją sprawdzającą, czy liczba leży w przedziale <x, y>
#
def in_range(number, x, y):
    # Warunek x <= number <= y obejmuje oba końce przedziału.
    # W Pythonie można zapisać porównanie łańcuchowo, zamiast używać 'and'.
    return x <= number <= y
