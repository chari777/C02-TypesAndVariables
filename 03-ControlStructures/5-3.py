N = 10
sum_even = 0
i = 1 # w pętli while sam muszę stworzyć licznik przed pętlą...

while i <= N:
    if i % 2 == 0:
        sum_even += i
    i += 1 # ...i sam muszę pamiętać, żeby zwiększać go o 1 na końcu, bo inaczej zrobię pętlę nieskończoną!

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")