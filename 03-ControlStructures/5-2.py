total_sum = 0
count = 0 # dokładam licznik, żeby wiedzieć przez ile liczb podzielić przy liczeniu średniej

# while True to celowa pętla nieskończona – przerwie ją dopiero instrukcja 'break'
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break # jak wpiszę 0, natychmiast wyskakuję z pętli (nie doliczam zera do sumy ani licznika)
        
    total_sum += number
    count += 1 # zwiększam licznik wpisanych liczb o 1

print(f"The total sum of the numbers is: {total_sum}")
if count > 0: # zabezpieczam się przed dzieleniem przez zero, gdyby ktoś od razu na start wpisał 0
    print(f"The arithmetic mean is: {total_sum / count}")