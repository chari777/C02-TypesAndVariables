i = 6 # zaczynam od górnego rzędu (6 + 1 = 7, 6 + 2 = 8, 6 + 3 = 9)

while i >= 0:
    j = 1 # przed każdym rzędem muszę zresetować licznik kolumn z powrotem na 1
    while j <= 3:
        print(f'{i + j}', end=' ') # end=' ' sprawia, że liczby drukują się obok siebie zamiast w nowej linii
        j += 1
    print() # pusty print() robi przejście do nowej linii po zakończeniu rzędu
    i -= 3  # schodzę o jeden rząd niżej (z 6 na 3, potem na 0)