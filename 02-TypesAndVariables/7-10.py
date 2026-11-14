import random

computer = random.randint(1, 6) # komputer po cichu losuje liczbę od 1 do 6
you = int(input('Guess the number (1-6): ')) # ja wpisuję swój strzał i zamieniam go na liczbę int()

won = computer == you # sprawdzam, czy mój strzał jest równy temu, co wylosował komputer
print(f'Computer rolled: {computer}')
print(f'You won: {won}')