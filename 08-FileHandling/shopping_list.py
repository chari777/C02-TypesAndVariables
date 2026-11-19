###
# Lista zakupów: użytkownik wpisuje produkty, każdy trafia do pliku shopping_list.txt.
# Wpisanie 0 kończy program.
#
shopping_list = 'shopping_list.txt'

# Dodaje nazwę produktu na koniec pliku.
# Tryb 'a' (append) dopisuje na końcu, nie kasuje istniejącej zawartości.
def add_product(file_name, product_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(product_name + '\n')

product = ""
while product != "0":
    product = input('Enter product name (0 stops): ')
    if product == '0':
        # Koniec pętli - nic nie zapisujemy dla '0'
        break
    add_product(shopping_list, product)

print('Shopping list saved to', shopping_list)
