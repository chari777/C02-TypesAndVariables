amount = int(input('Enter the amount in PLN: '))
print(f'The amount of PLN {amount} in coins:')

# dzielenie całkowite // mówi mi ile pełnych monet 5 zł mieści się w kwocie
coins_5 = amount // 5
amount = amount % 5 # reszta z dzielenia % to kwota, która została mi jeszcze do rozmienienia

coins_2 = amount // 2
coins_1 = amount % 2 # to co zostanie po dwuzłotówkach, muszę wydać w złotówkach

print(f'5 PLN coins: {coins_5}')
print(f'2 PLN coins: {coins_2}')
print(f'1 PLN coins: {coins_1}')