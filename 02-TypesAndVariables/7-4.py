password = input('Enter password: ')
password_ok = len(password) >= 8 # liczę znaki hasła i sprawdzam, czy jest ich co najmniej 8
print(f'Password length is valid: {password_ok}')