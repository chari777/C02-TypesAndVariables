login = 'joe'
password = 'abcd'

entered_login = input('Login: ')
entered_password = input('Password: ')

# oba warunki muszą być spełnione jednocześnie, dlatego używam 'and'
if login == entered_login and password == entered_password:
    print('You are logged in')
else:
    print('Incorrect login or password!!')