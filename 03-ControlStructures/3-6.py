age = int(input('Enter your age: '))

# wystarczy, że spełnię JEDEN z tych warunków, dlatego łączę je słówkiem 'or'
if age < 18 or age >= 65:
    print('Discount available')
else:
    print('No discount')