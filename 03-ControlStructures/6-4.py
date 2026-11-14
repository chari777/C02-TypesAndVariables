temperature = 32 # wpisuję temperaturę do sprawdzenia (np. 33, 30, 8, 0, -2)

if temperature > 35:
    print("It is extremely hot")
elif temperature > 30: # tu wpadnie zakres (30, 35], bo wyższe już wyłapał pierwszy 'if'
    print("It is hot")
elif temperature >= 15:
    print("It is warm")
elif temperature >= 0:
    print("It is cold")
else:
    print("Warning, frost") # wszystko poniżej zera