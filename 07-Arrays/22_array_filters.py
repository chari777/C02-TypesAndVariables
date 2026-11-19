# KROKI podziału na parzyste i nieparzyste:
# 1. Dwie puste listy: evens i odds.
# 2. Dla każdego x: x % 2 == 0 -> do evens, inaczej do odds.
# 3. arr = evens + odds - sklejenie list: najpierw parzyste, potem nieparzyste.
###
# Filtrowanie tablic: liczby większe od wartości, podział na parzyste i nieparzyste,
# podtablica, losowy element.
#
import random

# --- Ile elementów jest większych od podanej wartości ---
# Liczby rzeczywiste zamieniamy z napisu przez float()
values = [1.5, 7.2, 3.0, 9.8, 4.4, 6.1]
threshold = float(input('Enter a value: '))
count_greater = 0
for v in values:
    if v > threshold:
        count_greater += 1
print(f'Elements greater than {threshold}: {count_greater}')

# --- Parzyste na początku, potem nieparzyste ---
arr = [7, 9, 2, 4, 5, 6]
evens = []
odds = []
for x in arr:
    if x % 2 == 0:
        evens.append(x)
    else:
        odds.append(x)
# Łączymy listy: najpierw parzyste, potem nieparzyste
arr = evens + odds
print('Even first:', arr)

# --- Czy pierwsza tablica jest podzbiorem drugiej ---
# Każdy element pierwszej musi wystąpić w drugiej
def is_subset(first, second):
    for x in first:
        if x not in second:
            return False
    return True

print('Is [2,4] subset of [1,2,3,4]?', is_subset([2, 4], [1, 2, 3, 4]))
print('Is [2,5] subset of [1,2,3,4]?', is_subset([2, 5], [1, 2, 3, 4]))

# --- Losowy element tablicy ---
# random.choice() wybiera losowy element z listy
def rand_elem(array):
    return random.choice(array)

fruits = ['apple', 'pear', 'plum', 'cherry', 'kiwi']
for _ in range(3):
    print('Random element:', rand_elem(fruits))
