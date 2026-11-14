account_balance = 500
total_payment = int(input('Enter total payment: '))

# używam <= ("mniejsze lub równe"), bo jak mam 500 zł i zakupy kosztują 500 zł, to też mogę zapłacić
if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')