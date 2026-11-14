# tutaj używam float() zamiast int(), bo kwota może mieć grosze po kropce (np. 15.84)
amount = float(input('Enter amount: '))
vat = amount * 0.23

# zapis ':.2f' w klamrze wymusza pokazanie dokładnie 2 miejsc po przecinku (jak w cenach)
print(f'Amount  : {amount:.2f}')
print(f'VAT 23% : {vat:.2f}')