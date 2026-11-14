import math

circumference = float(input('Enter tree circumference in cm: '))
# wczytuję obwód drzewa, więc żeby dostać średnicę, dzielę obwód przez Pi (wzór: Obwód = Pi * średnica)
diameter = circumference / math.pi
can_cut_down = diameter >= 50 # sprawdzam, czy średnica ma co najmniej 50 cm
print(f'Tree can be cut down: {can_cut_down}')