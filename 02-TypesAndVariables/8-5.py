swift = input('Enter SWIFT code: ') # np. BPKOPLPW

# pierwsze 4 znaki to kod banku, a kolejne 2 (na indeksach 4 i 5) to kod kraju
print(f'Bank Code: {swift[0:4]}')
print(f'Country Code: {swift[4:6]}')