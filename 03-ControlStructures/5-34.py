import time # ładuję moduł czasu, żeby program naprawdę czekał 1 sekundę między liczbami

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0:
    # dla ostatnich 5 sekund wypisuję słowa zamiast cyfr
    if countdown == 5:
        print("five")
    elif countdown == 4:
        print("four")
    elif countdown == 3:
        print("three")
    elif countdown == 2:
        print("two")
    elif countdown == 1:
        print("one")
    else:
        print(countdown)
        
    countdown -= 1 # zmniejszam licznik o 1 sekundę
    time.sleep(1)  # usypiam program na 1 sekundę

print("Time's up!")