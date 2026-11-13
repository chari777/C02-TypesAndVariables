sum = 0 # tzw. akumulator – startuję od zera i będę tu dorzucać kolejne liczby

# w range(5, 11) druga liczba się nie wlicza, więc żeby dojść do 10 włącznie, muszę wpisać 11
for i in range(5, 11):
    sum += i # zapis sum += i to skrót od sum = sum + i

print(f'Sum is {sum}')