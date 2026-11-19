###
# Program korzystający z funkcji i stałych modułu math
#
# Aby użyć funkcji z zewnętrznego modułu, trzeba go najpierw zaimportować.
import math

# sqrt() liczy pierwiastek kwadratowy
square_root = math.sqrt(7)
print('A square root of 7 is', square_root)

# log() bez drugiego argumentu liczy logarytm NATURALNY (o podstawie e)
natural_log = math.log(5)
print('A natural logarithm of 5 is', natural_log)

# sin() w Pythonie przyjmuje kąt w RADIANACH, a nie w stopniach.
# Dlatego najpierw zamieniamy 90 stopni na radiany funkcją radians().
sine = math.sin(math.radians(90))
print('A sine of 90 degrees is', sine)
