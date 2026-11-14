current_price = 140.00
previous_price = 200.00

print(f'Current product price: {current_price:.2f}')
print(f'Previous product price: {previous_price:.2f}')

# obliczam procentowy spadek ceny
discount_percent = ((previous_price - current_price) / previous_price) * 100

if discount_percent >= 10:
    print('Buy the product!!')
    print(f'Product price reduced by {int(discount_percent)}%')