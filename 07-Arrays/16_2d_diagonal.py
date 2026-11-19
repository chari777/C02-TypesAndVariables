###
# Zamienia wartości na przekątnej macierzy kwadratowej na 1
#
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Na przekątnej wiersz i kolumna mają ten sam numer: matrix[i][i].
# Pętla przechodzi po indeksach i, więc zmienia dokładnie te pola.
for i in range(len(matrix)):
    matrix[i][i] = 1

# Wypisanie macierzy: w każdym wierszu liczby oddzielone spacją
for row in matrix:
    print(' '.join(str(value) for value in row))
