###
# Pobiera dane zakupionego produktu z klawiatury i zapisuje je do product.json
#
import json

product = {}

# Nazwa - napis (str). strip() usuwa zbędne spacje na początku i końcu.
product['name'] = input('Product name: ').strip()

# Cena - liczba rzeczywista (float). Zaokrąglamy do 2 miejsc po przecinku.
product['price'] = round(float(input('Price (e.g. 12.50): ').replace(',', '.')), 2)

# Czy zapłacono - wartość logiczna (bool). Odpowiedź tak/nie zamieniamy na True/False.
paid_answer = input('Paid? (yes/no): ').strip().lower()
product['paid'] = paid_answer in ('yes', 'y', 'tak', 't')

with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4, ensure_ascii=False)

print('Product data saved to product.json')
print(product)
