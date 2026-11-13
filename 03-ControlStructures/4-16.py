university = 'Krakow University of Economics'
university_expanded = '' # tworzę pusty napis, do którego będę po kolei doklejać litery w pętli

# pętla bierze po jednej literze z 'university' i wrzuca ją do zmiennej 'char'
for char in university:
    university_expanded = university_expanded + char + ' ' # doklejam literę i spację

print(university)
print(university_expanded)