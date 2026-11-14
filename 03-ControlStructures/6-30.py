# zewnętrzna pętla idzie po wierszach od 1 do 7
for row in range(1, 8):
    # wewnętrzna pętla skacze co 7 w prawo (np. dla wiersza 1: 1, 8, 15, 22, 29, 36, 43)
    for num in range(row, 50, 7):
        print(f'{num:2}', end=' ') # zapis :2 wyrównuje jednocyfrowe liczby spacją, żeby kolumny były równe
    print() # po każdym wierszu łamię linię