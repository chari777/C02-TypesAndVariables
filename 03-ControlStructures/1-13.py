speed_limit = 140
car_speed = int(input('Enter car speed (km/h): '))

# dwukropek na końcu i wcięcie (Tab) oznaczają, że poniższe linijki wykonają się TYLKO wtedy, gdy warunek jest prawdziwy
if car_speed > speed_limit:
    print(f'Your speed is {car_speed}km/h')
    print('Warning: speed limit exceeded!!')