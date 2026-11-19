# KROKI:
# 1. try: próbujemy otworzyć plik podany przez użytkownika.
# 2. except FileNotFoundError: pliku nie ma -> komunikat, program żyje dalej.
# 3. else: plik się otworzył -> liczymy linie (splitlines), znaki (len), słowa (split).
###
# Liczy linie, znaki i słowa w pliku podanym przez użytkownika.
# try-except zapobiega zawieszeniu programu, gdy plik nie istnieje.
#
file_name = input('File name: ')

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    # Ten blok wykona się tylko wtedy, gdy plik nie istnieje
    print(f'File {file_name} does not exist.')
else:
    # else wykonuje się tylko wtedy, gdy nie było błędu
    lines = content.splitlines()
    print(f'File name: {file_name}')
    print('Number of lines:', len(lines))
    # len(content) liczy wszystkie znaki, włącznie ze spacjami i znakami nowej linii
    print('Number of characters:', len(content))
    # split() bez argumentów dzieli po dowolnych białych znakach
    print('Number of words:', len(content.split()))
