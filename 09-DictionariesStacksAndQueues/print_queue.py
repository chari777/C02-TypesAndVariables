# KROKI (kolejka FIFO):
# 1. '1' -> put(): plik trafia na KONIEC kolejki.
# 2. '2' -> get(): zdejmujemy plik z POCZĄTKU (ten czekał najdłużej).
# 3. Jeśli kolejka pusta (empty()), wypisujemy komunikat zamiast próbować get().
###
# Zarządzanie kolejką wydruku plików. Kolejka działa jak w kolejce do kasy: FIFO.
#
import queue

# Kolejka plików do wydrukowania
files_to_print = queue.Queue()

while True:
    print('1. Add file to print')
    print('2. Print file')
    print('0. Quit')
    menu = input('Select an option: ')

    if menu == '1':
        file_name = input('Enter file name to print: ')
        # put() dodaje element na KONIEC kolejki
        files_to_print.put(file_name)
        print(f'File {file_name} added to the queue.')

    elif menu == '2':
        # empty() sprawdza, czy kolejka jest pusta
        if not files_to_print.empty():
            # get() zdejmuje element z POCZĄTKU kolejki (najstarszy)
            file_to_print = files_to_print.get()
            print(f'File {file_to_print} is currently being printed. Please wait!')
        else:
            print('The print queue is empty.')

    elif menu == '0':
        break
    else:
        print('Unknown option, try again.')
