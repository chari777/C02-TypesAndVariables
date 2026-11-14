decimal = int(input('Enter decimal number: '))
number = decimal # robię kopię liczby, żeby na końcu ładnie wypisać wartość początkową
binary = ''      # tu będę doklejać reszty z dzielenia od lewej strony

if number == 0:
    binary = '0'

while number > 0:
    remainder = number % 2 # biorę resztę z dzielenia przez 2 (0 albo 1)
    binary = str(remainder) + binary # doklejam resztę Z PRZODU (bo czytamy wynik od dołu do góry)
    number = number // 2 # dzielę całkowicie przez 2 i biorę wynik do kolejnego kroku

print(f'{decimal}(10) = {binary}(2)')