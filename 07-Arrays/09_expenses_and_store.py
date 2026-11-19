###
# Zadanie 1: która kategoria wydatków była najdroższa
# Zadanie 2: wartość wszystkich towarów w sklepie
#

# --- Zadanie 1 ---
categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# max() zwraca największą kwotę. index() mówi, na którym miejscu ona stoi.
# Ten sam indeks wskazuje odpowiednią nazwę kategorii w liście categories.
highest_value = max(expenses)
highest_index = expenses.index(highest_value)
print(f'The most expensive category is {categories[highest_index]} ({highest_value})')

# --- Zadanie 2 ---
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

# zip() łączy dwie listy w pary (cena, ilość) - pierwszy z pierwszym, drugi z drugim
total_value = 0
for price, quantity in zip(product_prices, product_quantities):
    total_value += price * quantity

# round(..., 2) zaokrągla do 2 miejsc po przecinku (wartości pieniężne)
print('Total value of all goods in the store:', round(total_value, 2))
