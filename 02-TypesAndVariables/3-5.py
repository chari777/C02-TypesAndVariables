import math # muszę zaimportować bibliotekę math, bo sam Python nie ma funkcji pierwiastka

a = 5
b = 8
# dwie gwiazdki ** to potęgowanie, a math.sqrt() liczy pierwiastek kwadratowy (twierdzenie Pitagorasa)
diagonal = math.sqrt(a**2 + b**2)

print("Diagonal:", round(diagonal, 2))