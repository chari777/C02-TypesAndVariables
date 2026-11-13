speed = int(input('Enter vehicle speed: '))
# oba warunki muszą być spełnione naraz, dlatego łączę je słówkiem 'and'
speed_ok = speed >= 40 and speed <= 140
print(f'Speed is valid: {speed_ok}')