###
# Wypisuje elementy tablicy (w Pythonie tablicą nazywamy zwykle listę)
#
# Lista jest tworzona w nawiasach [], a elementy numerowane są od 0.
arr = [2, 3, 7, 5, 4]

print('Array:', arr)
# len() zwraca liczbę elementów listy
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
# Ostatni element: indeks len(arr)-1 (bez używania ujemnych indeksów)
print('Last value', arr[len(arr) - 1])
# Przedostatni element: o jeden przed ostatnim
print('Last but one value', arr[len(arr) - 2])
print('Sum of the first and last value', arr[0] + arr[len(arr) - 1])
# Środkowy element: dla 5 elementów to indeks 2 (dzielenie // daje część całkowitą)
print('Middle value', arr[len(arr) // 2])

# Wypisanie wszystkich elementów w jednej linii, oddzielonych spacją.
# end=' ' nie przechodzi do nowej linii po każdym elemencie.
for value in arr:
    print(value, end=' ')
# Pusty print() dodaje znak nowej linii na koniec
print()
