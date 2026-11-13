# 1. Wczytuję temperaturę w stopniach Celsjusza
celsius = float(input('Enter temperature in Celsius: '))

# 2. Przeliczam na Kelwiny i Fahrenheity ze standardowych wzorów
kelvin = celsius + 273.15
fahrenheit = (celsius * 9 / 5) + 32

# 3. Wyświetlam oba wyniki zaokrąglone do 2 miejsc po przecinku
print(f'Kelvin: {kelvin:.2f}')
print(f'Fahrenheit: {fahrenheit:.2f}')