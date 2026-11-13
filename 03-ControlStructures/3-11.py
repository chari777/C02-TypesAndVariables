x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

# "nieujemna" znaczy większa lub równa 0 (czyli "not x < 0" to dokładnie to samo co "x >= 0")
if not x < 0 or not y < 0:
    print(f'At least one of the numbers {x} and {y} is not negative')
else:
    print(f'Both numbers {x} and {y} are negative')