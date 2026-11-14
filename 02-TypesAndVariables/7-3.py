number = int(input('Enter number: '))
# znak % (modulo) daje resztę z dzielenia; jeśli reszta z dzielenia przez 2 wynosi 0, liczba jest parzysta
even = number % 2 == 0 # pamiętam, że dwa znaki == to porównanie ("czy jest równe?"), a jeden = to przypisanie
print(f'Number is even: {even}')