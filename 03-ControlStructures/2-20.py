number1 = float(input('Enter first number: ')) # używam float, żeby kalkulator działał też na ułamkach
number2 = float(input('Enter second number: '))
operator = input('Enter operator (+, -, *, /): ')

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2
else:
    result = 'Unknown operator'

print(f'{number1} {operator} {number2} = {result}')