x = 7
y = 34
z = 0 # zrobiłem pustą zmienną pomocniczą ("trzecią szklankę"), żeby nie stracić wartości przy zamianie

print("Before swapping: x=", x, "y=", y)

z = x # najpierw chowam wartość x (czyli 7) do z, żeby jej nie nadpisać i nie zgubić
x = y # teraz mogę bezpiecznie wrzucić wartość y (34) do x
y = z # na koniec wyciągam schowane 7 ze zmiennej z i wrzucam do y

print("After swapping: x=", x, "y=", y)