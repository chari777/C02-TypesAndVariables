###
# Macierz jednostkowa, transpozycja i spłaszczenie tablicy 2D do 1D
#

# Macierz jednostkowa n x n: 1 na przekątnej, 0 wszędzie indziej
def identity_matrix(n):
    # Pole (i, j) jest na przekątnej, gdy i == j
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# Wypisuje macierz w wierszach i kolumnach
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(v) for v in row))

# Transpozycja: zamiana wierszy z kolumnami.
# Element (r, c) przechodzi na pozycję (c, r).
def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])
    return [[m[r][c] for r in range(rows)] for c in range(cols)]

# Spłaszczenie: wszystkie elementy w jednej liście, wiersz po wierszu
def flatten(matrix):
    result = []
    for row in matrix:
        for value in row:
            result.append(value)
    return result

if __name__ == "__main__":
    # Trzy macierze jednostkowe
    for size in [3, 5, 8]:
        print(f'Identity matrix {size}x{size}:')
        print_matrix(identity_matrix(size))
        print()

    # Transpozycje z zadania
    print('Transpose 1:')
    print_matrix(transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print()
    print('Transpose 2:')
    print_matrix(transpose_matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]))
    print()
    print('Transpose 3:')
    print_matrix(transpose_matrix([[5, 6, 7, 8]]))
    print()

    # Spłaszczenie
    print('Flatten 1:', flatten([[2, 3], [1, 5]]))
    print('Flatten 2:', flatten([[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]]))
    print('Flatten 3:', flatten([[2, 1], [3, 5], [7, 4], [2, 6]]))
