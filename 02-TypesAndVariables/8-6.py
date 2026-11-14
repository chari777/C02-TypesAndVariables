distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption (L/100km): '))

total_fuel_consumption = distance * (fuel_consumption / 100) # liczę ile litrów spali na całej trasie
total_cost = total_fuel_consumption * fuel_price             # mnożę litry przez cenę za litr

print(f'Total fuel consumed: {total_fuel_consumption:.2f} L')
print(f'Total transport cost: {total_cost:.2f}')