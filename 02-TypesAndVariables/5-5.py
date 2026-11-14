price = float(input('Enter price: '))
discount = float(input('Enter discount %: '))

reduction = price * (discount / 100) # wyliczam ile złotych wynosi sam rabat
new_price = price - reduction # odejmuję rabat od ceny wyjściowej

print(f'Price with discount: {new_price:.2f}')
print(f'Reduction: {reduction:.2f}')