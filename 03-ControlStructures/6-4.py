light_switch1 = False # False - wyłączony, True - włączony
light_switch2 = False
bulbs_on = 0

if light_switch1:
    bulbs_on += 1 # pierwszy włącznik zapala 1 żarówkę
if light_switch2:
    bulbs_on += 2 # drugi włącznik zapala 2 żarówki

print(f"Number of bulbs lit: {bulbs_on}")