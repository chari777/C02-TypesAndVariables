speed_kmh = 70
speed_ms = speed_kmh / 3.6 # żeby zamienić km/h na m/s, muszę podzielić przez 3.6

# użyłem round(..., 2), bo inaczej wyszedłby brzydki ułamek z mnóstwem cyfr po przecinku
print(speed_kmh, "km/h = ", round(speed_ms, 2), "m/s")