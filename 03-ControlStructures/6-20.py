count = int(input('Number of products purchased: '))
price = float(input('Product price: '))

if count <= 2:
    total = count * price # brak rabatu przy 1 lub 2 sztukach
else:
    # pierwsze 2 sztuki płacę w pełnej cenie, a resztę (count - 2) z rabatem 25% (czyli płacę 75% ceny)
    total = (2 * price) + (count - 2) * (price * 0.75)

print(f'Amount to pay: {total:.2f}')