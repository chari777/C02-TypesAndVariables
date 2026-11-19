# KROKI:
# Każdy nowy klient dostaje numer z licznika next_ticket_number, który rośnie o 1.
# Klient wchodzi na koniec kolejki (put). Obsługujemy zawsze pierwszego (get).
# Dlaczego kolejka, a nie stos? W urzędzie pierwszy przyszedł -> pierwszy obsłużony (FIFO).
###
# Obsługa klientów w urzędzie: każdy klient dostaje kolejny numer biletu
# i trafia na koniec kolejki. Obsługujemy zawsze pierwszą osobę w kolejce.
#
import queue

tickets = queue.Queue()
next_ticket_number = 1   # numer dla kolejnego klienta

while True:
    print('1. Take a ticket')
    print('2. Serve next customer')
    print('0. Quit')
    choice = input('Select an option: ')

    if choice == '1':
        # Każdy nowy klient dostaje numer i wędruje na koniec kolejki
        tickets.put(next_ticket_number)
        print(f'Your ticket number is {next_ticket_number}.')
        next_ticket_number += 1
    elif choice == '2':
        if tickets.empty():
            print('No customers are waiting.')
        else:
            # get() zdejmuje klienta z początku kolejki
            print(f'Serving customer with ticket number {tickets.get()}.')
    elif choice == '0':
        break
    else:
        print('Unknown option.')
