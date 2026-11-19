###
# Stan magazynowy sklepu komputerowego: lista produktów, ilości i ich suma
#
products = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}

print('PRODUCTS IN STOCK')
print('-----------------')
total = 0
for product, quantity in products.items():
    print(f'{product}: {quantity}')
    # Sumujemy ilości wszystkich produktów
    total += quantity

print('-----------------')
print('Total number of products:', total)
