# KROKI:
# 1. Tablica startowa [1,2,3,4,5].
# 2. arr[0] = arr[0] - 1 -> pierwszy element zmniejszony.
# 3. arr[-1] = arr[-1] + 4 -> ostatni element zwiększony.
# 4. arr[len//2] - środkowy element mnożymy przez 2.
# Po każdej zmianie show() wypisuje tablicę.
###
# Modyfikacja wartości tablicy i wypisywanie jej po każdej zmianie
#
arr = [1, 2, 3, 4, 5]

# Funkcja pomocnicza: zamienia listę na napis w formacie [a,b,c]
# join() skleja napisy z przecinkami; map(str, ...) zamienia liczby na napisy
def show(array):
    print('Array: [' + ','.join(map(str, array)) + ']')

show(arr)

# 1. Odejmujemy 1 od pierwszego elementu (indeks 0)
arr[0] = arr[0] - 1
show(arr)

# 2. Zwiększamy ostatni element o 4 (indeks -1 to ostatni element)
arr[-1] = arr[-1] + 4
show(arr)

# 3. Mnożymy element środkowy (indeks 2) przez 2
arr[len(arr) // 2] = arr[len(arr) // 2] * 2
show(arr)
