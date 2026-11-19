###
# Tworzy kopię pliku healthy_lifestyle.txt jako copy_healthy_lifestyle.txt
#

# Nazwy plików: oryginał i kopia
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# Najpierw czytamy CAŁĄ zawartość oryginału do zmiennej
with open(original_file, 'r', encoding='utf-8') as file:
    content = file.read()

# Potem zapisujemy tę zawartość do nowego pliku.
# Oba pliki są otwarte osobno, bo jeden jest w trybie odczytu, drugi zapisu.
with open(target_file, 'w', encoding='utf-8') as file:
    file.write(content)

print(f'{original_file} has been copied to {target_file}.')
