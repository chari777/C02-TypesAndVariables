###
# Tworzenie różnych tablic. Na końcu wypisujemy każdą z nich.
#
import random

arr1 = [3, 7, 1, 0, 4]
arr2 = [[2, 3], [7, 1], [0, 4]]
# Wyrażenie: [wartość for i in range(5)] tworzy listę 5 elementów
arr3 = [7 for i in range(5)]
arr4 = [i for i in range(1, 10)]
arr5 = [i * 2 for i in range(1, 10)]
arr6 = [random.randint(1, 20) for i in range(10)]
arr7 = [[] for i in range(5)]
arr8 = [[1 for i in range(2)] for j in range(4)]
arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]

# Tablice opisane słownie w zadaniu
arr_4_0_3 = [4, 0, 3]
arr_zeros = [0] * 15
arr_random_1_30 = [random.randint(1, 30) for _ in range(10)]
arr_random_0_1 = [random.randint(0, 1) for _ in range(20)]
# UWAGA: [[False] * 2] * 5 powieliłoby JEDEN wiersz 5 razy (wszystkie wiersze to ten sam obiekt).
# Dlatego tworzymy nowy wiersz w każdej iteracji.
arr_false = [[False] * 2 for _ in range(5)]

for name, value in [('arr1', arr1), ('arr2', arr2), ('arr3', arr3), ('arr4', arr4),
                    ('arr5', arr5), ('arr6', arr6), ('arr7', arr7), ('arr8', arr8),
                    ('arr9', arr9), ('4,0,3', arr_4_0_3), ('zeros', arr_zeros),
                    ('random 1-30', arr_random_1_30), ('random 0/1', arr_random_0_1),
                    ('False 5x2', arr_false)]:
    print(f'{name}: {value}')
