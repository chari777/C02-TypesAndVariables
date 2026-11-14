balance = 1000 # początkowe saldo
pin = '1111'   # przechowuję PIN jako tekst (str), bo może zaczynać się od zera (np. '0805')

while True:
    print("\nATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print(f"Your current PIN is: {pin}")
    elif choice == '5':
        new_pin = input("Enter new 4-digit PIN: ")
        # len(new_pin) == 4 sprawdza długość, a .isdigit() sprawdza czy wszystkie znaki to cyfry
        if len(new_pin) == 4 and new_pin.isdigit():
            pin = new_pin
            print("PIN has been changed.")
        else:
            print("Invalid PIN. Must be exactly 4 digits.")
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break # wychodzę z głównej pętli menu i kończę program
    else:
        print("Invalid option. Please try again.")