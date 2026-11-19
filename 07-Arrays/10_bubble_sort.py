# KROKI SORTOWANIA BĄBELKOWEGO na przykładzie [3, 1, 2]:
# Przejście 1: porównaj 3 i 1 -> zamiana -> [1,3,2]; porównaj 3 i 2 -> zamiana -> [1,2,3]
# Przejście 2: porównaj 1 i 2 -> bez zmian. Koniec, bo nic się nie zamieniło.
# Zewnętrzna pętla (i) = liczba przejść.
# Wewnętrzna pętla (j) = pary sąsiednich elementów; zakres n-i-1, bo końcówka jest już posortowana.
###
# Sortowanie bąbelkowe (bubble sort) - funkcja sortuje tablicę liczb.
#
# Idea: porównujemy sąsiednie elementy i zamieniamy je miejscami,
# jeśli są w złej kolejności. Po każdym przejściu największy element
# "wypływa" na koniec, jak bąbelek w wodzie.
def bubble_sort(arr):
    # n to liczba elementów. range(n) daje liczby 0..n-1
    n = len(arr)
    # Zewnętrzna pętla: wykonuje tyle przejść, ile elementów
    for i in range(n):
        # Wewnętrzna pętla: porównuje sąsiednie pary.
        # n-i-1: po każdym przejściu ostatnie elementy są już na miejscu,
        # więc nie sprawdzamy ich ponownie.
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Zamiana miejscami z wykorzystaniem przypisania równoległego
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)
print(sorted_car_fuel_consumption)

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print(bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print(sorted_bank_transactions)
