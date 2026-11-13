a = 0 # pierwszy wyraz ciągu
b = 1 # drugi wyraz ciągu

for i in range(20):
    print(a, end=' ')
    # przesuwam się dalej: nowym 'a' staje się stare 'b', a nowym 'b' suma obu poprzednich
    next_term = a + b
    a = b
    b = next_term