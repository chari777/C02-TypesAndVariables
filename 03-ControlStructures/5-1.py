import random

number_to_guess = random.randint(1, 100) # komputer losuje tajną liczbę
user_guess = 0 # ustawiam 0 na start, żeby warunek w pętli od razu był prawdziwy

print("Guess the number between 1 and 100!")

# kręcę pętlą tak długo, jak długo mój strzał różni się od wylosowanej liczby
while user_guess != number_to_guess:
    user_guess = int(input("Enter your guess: "))

    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")