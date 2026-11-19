###
# Wyprzedaż: 10% zniżki na każdy produkt w sklepie odzieżowym
#
price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

print('PRICES BEFORE DISCOUNT')
total_before = 0
for product, price in price_list.items():
    print(f'{product}: {price:.2f}')
    total_before += price
print(f'Total value before discount: {total_before:.2f}')

# Modyfikujemy słownik w miejscu: nowa cena = 90% starej.
# round(..., 2) zaokrągla do groszy.
for product in price_list:
    price_list[product] = round(price_list[product] * 0.9, 2)

print()
print('PRICES AFTER 10% DISCOUNT')
total_after = 0
for product, price in price_list.items():
    print(f'{product}: {price:.2f}')
    total_after += price
print(f'Total value after discount: {total_after:.2f}')
