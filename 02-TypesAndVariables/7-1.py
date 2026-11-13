age = int(input('Enter age: '))
no_tax = age <= 26 # sprawdzam warunek "mniejsze lub równe 26" – wynik to od razu True albo False
print(f'Exemption from paying taxes: {no_tax}')