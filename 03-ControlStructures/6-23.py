for i in range(1, 31):
    # warunek podzielności przez oba (3 i 5) MUSI być pierwszy, bo inaczej wyłapałby go już pierwszy 'if' dla trójki!
    if i % 3 == 0 and i % 5 == 0:
        print('BINGO', end=' ')
    elif i % 3 == 0:
        print('THREE', end=' ')
    elif i % 5 == 0:
        print('FIVE', end=' ')
    else:
        print(i, end=' ')