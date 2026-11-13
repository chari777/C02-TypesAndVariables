human_years = int(input("Enter the dog's age in human years: "))

if human_years <= 2:
    dog_years = human_years * 10.5 # pierwsze dwa lata liczą się po 10.5
else:
    # pierwsze 2 lata dają 21, a każdy kolejny rok powyżej dwóch mnożę przez 4
    dog_years = 2 * 10.5 + (human_years - 2) * 4

print(f"The dog's age in dog's years is {int(dog_years)} years.")