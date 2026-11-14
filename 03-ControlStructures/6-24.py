# pierwsza pętla rysuje górną połowę (od 1 do 5 gwiazdek)
for i in range(1, 6):
    print('* ' * i) # mnożenie tekstu przez liczbę powiela ten tekst tyle razy

# druga pętla rysuje dolną połowę (od 4 w dół do 1 gwiazdki; krok -1 oznacza odliczanie wstecz)
for i in range(4, 0, -1):
    print('* ' * i)