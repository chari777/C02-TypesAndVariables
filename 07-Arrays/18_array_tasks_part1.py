###
# Zadania z tablicami - część 1
#

# --- Liczba parzystych wartości (pętla while) ---
numbers = [34, 7, 19, 4, 21, 8]
even_count = 0
i = 0
while i < len(numbers):
    # % 2 == 0 oznacza liczbę parzystą
    if numbers[i] % 2 == 0:
        even_count += 1
    i += 1
print('Number of even values:', even_count)

# --- Elementy w odwrotnej kolejności ---
nums = [15, 8, 31, 47, 2, 19]
reverse = []
# Idziemy od ostatniego indeksu do pierwszego: range(start, stop, krok)
for i in range(len(nums) - 1, -1, -1):
    reverse.append(nums[i])
print('existed array:', ' '.join(map(str, nums)))
print('reverse array:', ' '.join(map(str, reverse)))

# --- Kwadrat każdego elementu ---
arr = [8, 2, 5, 1, 9]
squares = [x ** 2 for x in arr]   # ** to potęgowanie
print('Array:', ' '.join(map(str, arr)))
print('2nd power:', ' '.join(map(str, squares)))

# --- Maksimum i minimum BEZ funkcji max() i min() ---
values = [-15, 8, -31, 47, -2, 19]
largest = values[0]
smallest = values[0]
for v in values:
    if v > largest:
        largest = v
    if v < smallest:
        smallest = v
print('Maximum:', largest)
print('Minimum:', smallest)

# --- Średnia arytmetyczna: pętla for ---
data = [15, 8, 31, 47, 2, 19]
total = 0
for v in data:
    total += v
mean = total / len(data)
print('Array:', data)
print(f'Arithmetic mean (for): {mean:.2f}')

# --- Średnia arytmetyczna: pętla while ---
i = 0
total = 0
while i < len(data):
    total += data[i]
    i += 1
print(f'Arithmetic mean (while): {total / len(data):.2f}')

# --- Najdłuższe imię ---
names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
longest = names[0]
for name in names:
    # len() zwraca liczbę znaków w napisie
    if len(name) > len(longest):
        longest = name
print('Names:', ' '.join(names))
print('Longest name:', longest)
