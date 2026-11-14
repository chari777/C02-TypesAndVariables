number = int(input('Enter number: '))

# jeśli reszta z dzielenia przez 2 wynosi 0, liczba dzieli się na 2 bez reszty, czyli jest parzysta
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')