# KROKI occurs(): przeglądamy tablicę po kolei.
# Jeśli element == szukana liczba -> return True od razu (nie musimy szukać dalej).
# Jeśli pętla skończyła się bez trafienia -> return False.
# To samo zadanie można zrobić jedną linią: number in array (ale tu pokazujemy pętlę).
###
# Zadania z tablicami - część 2
#

# --- Gwiazdki zamiast liczb ---
# Funkcja star zwraca n gwiazdek jako napis
def star(n):
    return '*' * n

for value in [2, 6, 4, 9, 7]:
    print(f'{value}: {star(value)}')

# --- Porównanie dwóch tablic ---
# Tablice są takie same, gdy mają tyle samo elementów i te same wartości na tych samych miejscach
def compare(array1, array2):
    # Różna długość = różne tablice
    if len(array1) != len(array2):
        return False
    # Sprawdzamy każdą parę elementów o tym samym indeksie
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

pairs = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2]),
]
for a1, a2 in pairs:
    result = 'arrays are the same' if compare(a1, a2) else 'arrays are different'
    print('Array1:', ' '.join(map(str, a1)))
    print('Array2:', ' '.join(map(str, a2)))
    print('Comparison:', result)
    print()

# --- Liczby z pierwszej tablicy, których nie ma w drugiej ---
first = [4, 36, 12, 28, 9, 44, 5]
second = [5, 1, 36]
missing = []
for x in first:
    # 'not in' sprawdza, czy wartość występuje w liście
    if x not in second:
        missing.append(x)
print('Numbers from the first array not in the second:', missing)

# --- Sortowanie bąbelkowe trzech tablic ---
def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

for test in [[5, 2, 9, 1], [10, -3, 7, 0, 2], [8, 8, 1]]:
    # Funkcja sortuje tablicę W MIEJSCU (zmienia oryginał), więc przekazujemy
    # kopię - dzięki temu możemy wypisać też stan przed sortowaniem.
    print('Before:', test, 'After:', bubblesort(test.copy()))

# --- Unikalne elementy: występują w tablicy dokładnie raz ---
arr = [2, 3, 2, 5, 8, 1, 9, 8]
unique = []
for x in arr:
    # count() zlicza wystąpienia wartości w liście
    if arr.count(x) == 1:
        unique.append(x)
print('Array:', ' '.join(map(str, arr)))
print('Unique elements:', ' '.join(map(str, unique)))

# --- Czy liczba występuje w tablicy ---
# Funkcja zwraca True/False w zależności od obecności liczby w tablicy
def occurs(number, array):
    for x in array:
        if x == number:
            return True
    return False

known = [15, 38, 7, 23, 14]
number = int(input('Number: '))
print('Array:', ' '.join(map(str, known)))
if occurs(number, known):
    print(f'Result: number {number} appears in the array')
else:
    print(f'Result: number {number} does not appear in the array')
