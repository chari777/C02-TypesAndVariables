n = int(input('Enter how many prime numbers to find: '))
found = 0     # licznik znalezionych już liczb pierwszych
candidate = 2 # pierwsza liczba, którą zaczynam sprawdzać (0 i 1 nie są pierwsze)

print('Prime numbers:', end=' ')

while found < n:
    is_prime = True # zakładam na start, że kandydat jest liczbą pierwszą
    
    # sprawdzam czy kandydat dzieli się bez reszty przez jakąkolwiek liczbę od 2 do (candidate - 1)
    for divisor in range(2, candidate):
        if candidate % divisor == 0:
            is_prime = False # znalazłem dzielnik, więc to NIE jest liczba pierwsza
            break
            
    if is_prime:
        print(candidate, end=' ')
        found += 1 # zaliczam kolejną znalezioną liczbę pierwszą
        
    candidate += 1 # biorę kolejną liczbę na warsztat