cm = 170

# 1 cal to 2.54 cm, więc najpierw przeliczam cały wzrost na łączną liczbę cali (zaokrągloną)
total_inches = round(cm / 2.54)

# 1 stopa ma 12 cali:
feet = total_inches // 12  # operator // (dzielenie całkowite) daje mi pełną liczbę stóp
inches = total_inches % 12 # operator % (reszta z dzielenia) daje mi pozostałe cale

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')