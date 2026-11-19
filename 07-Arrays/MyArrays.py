# KROKI MEDIANY:
# 1. Sortujemy KOPIĘ tablicy (oryginał zostaje bez zmian).
# 2. Nieparzysta liczba elementów: środkowy element to mediana.
# 3. Parzysta liczba: średnia z dwóch środkowych elementów.
# Nie używamy max/min/sorted, bo polecenie tego zabrania - wszystko liczymy pętlami.
###
# Moduł MyArrays - funkcje do operacji na tablicy liczb.
#
# Zgodnie z poleceniem NIE używamy wbudowanych funkcji (max, min, sorted, len itp.).
# Wszystko liczymy pętlami.


# Liczy elementy tablicy, bo len() nie jest tu dozwolone
def _count(array):
    # Znak _ na początku nazwy sygnalizuje, że to funkcja "wewnętrzna" modułu
    total = 0
    for _ in array:
        total += 1
    return total


# Sortuje kopię tablicy (żeby nie psuć oryginału) - potrzebne do mediany
def _sorted_copy(array):
    copy = []
    for x in array:
        copy.append(x)
    n = _count(copy)
    for i in range(n):
        for j in range(n - i - 1):
            if copy[j] > copy[j + 1]:
                copy[j], copy[j + 1] = copy[j + 1], copy[j]
    return copy


# Zwraca drugą największą wartość w tablicy.
# Śledzimy dwie wartości: największą i drugą co do wielkości.
def second_largest(array):
    largest = array[0]
    second = None
    for x in array:
        if x > largest:
            # Stare maksimum staje się drugim największym
            second = largest
            largest = x
        elif x != largest and (second is None or x > second):
            second = x
    return second


# Różnica między największą a najmniejszą wartością
def max_min_difference(array):
    largest = array[0]
    smallest = array[0]
    for x in array:
        if x > largest:
            largest = x
        if x < smallest:
            smallest = x
    return largest - smallest


# Mediana: środkowa wartość po posortowaniu.
# Dla parzystej liczby elementów bierzemy średnią dwóch środkowych.
def median(array):
    ordered = _sorted_copy(array)
    n = _count(ordered)
    middle = n // 2
    if n % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


# Zwraca dwuelementową tablicę: [najmniejsza, największa]
def min_max(array):
    smallest = array[0]
    largest = array[0]
    for x in array:
        if x < smallest:
            smallest = x
        if x > largest:
            largest = x
    return [smallest, largest]


# Zamienia tablicę na napis z wartościami oddzielonymi minusem
def to_string(array):
    text = ''
    for i in range(_count(array)):
        if i > 0:
            text += '-'
        text += str(array[i])
    return text
