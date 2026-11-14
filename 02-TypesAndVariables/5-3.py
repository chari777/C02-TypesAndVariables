# skróciłem zapis: od razu wrzucam input() do środka int(), żeby nie tworzyć osobnych zmiennych tekstowych
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

volume = a * b * c # objętość to iloczyn trzech krawędzi
surface_area = 2 * (a * b + a * c + b * c) # pole całkowite to suma pól wszystkich 6 ścian (po 2 takie same)

print(f'Volume = {volume}, surface area = {surface_area}')