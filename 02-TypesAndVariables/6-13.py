employee = "Mr. John May, born on 1998-02-16"

# zapis [start:koniec] wycina kawałek tekstu od indeksu 'start' do 'koniec - 1' (ostatni się nie wlicza)
print(f'Name: {employee[4:8]}')        # wycinam od 4 do 7 znaku -> 'John'
print(f'Surname: {employee[9:12]}')    # wycinam od 9 do 11 znaku -> 'May'
print(f'Born: {employee[-10:]}')       # minus oznacza liczenie od końca: biorę 10 ostatnich znaków (datę)
print(f'Initials: {employee[4]}{employee[9]}') # łączę pojedyncze litery z pozycji 4 i 9