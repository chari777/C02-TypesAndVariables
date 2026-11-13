sum = 0

for i in range(1, 11):
    # jeśli reszta z dzielenia przez 2 NIE jest zerem (liczba nieparzysta), pomijam ją i skaczę do następnego obrotu pętli
    if not i % 2 == 0:
        continue
    sum += i # ta linijka wykona się tylko dla liczb parzystych

print(f'Sum of even numbers in the range <1,10> is {sum}')