###
# Zadania z dwuwymiarowymi tablicami (listami list)
#

# --- Wypisanie tablicy 2x4 w wierszach i kolumnach ---
arr_2x4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
for row in arr_2x4:
    print(' '.join(str(v) for v in row))
print()

# --- Suma wartości w ostatniej kolumnie ---
table = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]
last_column_sum = 0
for row in table:
    # row[-1] to ostatni element wiersza, czyli wartość w ostatniej kolumnie
    last_column_sum += row[-1]
print('Sum of the last column:', last_column_sum)
print()

# --- Funkcja tworząca tablicę zer o wymiarach x na y ---
def create_2d_arr(x, y):
    # x wierszy, każdy wiersz ma y elementów
    return [[0] * y for _ in range(x)]

arr_3x5 = create_2d_arr(3, 5)
for row in arr_3x5:
    print(row)
print()

# --- Tabliczka mnożenia 5x5 ---
size = 5
table_mul = create_2d_arr(size, size)
for i in range(size):
    for j in range(size):
        # Wiersz i, kolumna j: wartość = (i+1) * (j+1)
        table_mul[i][j] = (i + 1) * (j + 1)
for row in table_mul:
    # >2 wyrównuje liczby do prawej na szerokość 2 znaków
    print(' '.join(f'{v:>2}' for v in row))
print()

# --- Najmniejsza i największa wartość oraz jej położenie ---
numbers = [[-38, 19], [5, 40], [-7, 11], [29, 16]]
smallest = numbers[0][0]
largest = numbers[0][0]
small_pos = (0, 0)
large_pos = (0, 0)
for r in range(len(numbers)):
    for c in range(len(numbers[r])):
        if numbers[r][c] < smallest:
            smallest = numbers[r][c]
            small_pos = (r, c)
        if numbers[r][c] > largest:
            largest = numbers[r][c]
            large_pos = (r, c)
print(f'Smallest value {smallest} at row {small_pos[0]}, column {small_pos[1]}')
print(f'Largest value {largest} at row {large_pos[0]}, column {large_pos[1]}')
print()

# --- Zamiana pierwszego i ostatniego wiersza ---
grid = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]
print('Before row swap:')
for row in grid:
    print(' '.join(str(v) for v in row))
# Przypisanie równoległe zamienia całe wiersze miejscami
grid[0], grid[-1] = grid[-1], grid[0]
print('After row swap:')
for row in grid:
    print(' '.join(str(v) for v in row))
print()

# --- Zamiana pierwszej i ostatniej kolumny ---
grid2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]
print('Before column swap:')
for row in grid2:
    print(' '.join(str(v) for v in row))
# Dla każdego wiersza zamieniamy pierwszy i ostatni element
for row in grid2:
    row[0], row[-1] = row[-1], row[0]
print('After column swap:')
for row in grid2:
    print(' '.join(str(v) for v in row))
