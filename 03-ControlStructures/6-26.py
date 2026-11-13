time_24 = input('Enter time (24-hour format, e.g. 16:32): ')

# wycinam pierwsze dwie cyfry (godzinę) i zamieniam na liczbę, a minuty zostawiam jako tekst po dwukropku
hours = int(time_24[0:2])
minutes = time_24[3:5]

if hours == 0:
    print(f'Time in 12-hour format: 12:{minutes}am')
elif hours < 12:
    print(f'Time in 12-hour format: {hours}:{minutes}am')
elif hours == 12:
    print(f'Time in 12-hour format: 12:{minutes}pm')
else:
    # dla godzin po południu (13-23) odejmuję 12, żeby dostać format 1-11pm
    print(f'Time in 12-hour format: {hours - 12}:{minutes}pm')