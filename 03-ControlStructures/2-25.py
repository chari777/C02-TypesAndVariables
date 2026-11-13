month = int(input('Enter month number (1..12): '))

# sprawdzam od najwyższego kwartału w dół – skoro nie jest >= 10, to w kolejnym kroku na pewno jest mniejszy niż 10
if month >= 10:
    quarter = 4
elif month >= 7:
    quarter = 3
elif month >= 4:
    quarter = 2
else:
    quarter = 1

print(f'Month {month} is in quarter {quarter}')