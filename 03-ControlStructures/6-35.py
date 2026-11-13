correct_pin = '0805'
attempts = 0

while attempts < 3:
    entered_pin = input('Enter the PIN code: ')
    if entered_pin == correct_pin:
        print('PIN correct! Payment accepted.')
        break # jak trafiłem PIN, od razu przerywam pętlę
    else:
        print('Incorrect...')
        attempts += 1 # zwiększam licznik nieudanych prób

# jeśli wykorzystałem wszystkie 3 próby i żadna nie była trafiona, blokuję kartę
if attempts == 3:
    print('Sorry, your payment card has been blocked.')