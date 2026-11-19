###
# Oblicza wartość koszyka zakupów na podstawie cennika
#
# Cennik: nazwa produktu -> cena jednostkowa
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Koszyk: nazwa produktu -> ilość sztuk
cart = {'juice': 3, 'bread': 1, 'milk': 2}

total = 0
for product, quantity in cart.items():
    # Cenę pobieramy z cennika po nazwie produktu, mnożymy przez ilość
    line_cost = prices[product] * quantity
    print(f'{product} x{quantity}: {line_cost:.2f}')
    total += line_cost

print(f'Total cost: {round(total, 2):.2f}')
