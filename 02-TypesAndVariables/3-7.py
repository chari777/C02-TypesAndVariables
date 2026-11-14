total = 8000000000 # duże liczby zapisuję bez spacji i kropek
north = 7200000000
south = total - north # reszta ludzi na świecie musi mieszkać na półkuli południowej

print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north / total * 100) # dzielę część przez całość i mnożę przez 100, żeby mieć procent
print("Southern Hemisphere: ", south)
print("Southern Hemisphere in %: ", south / total * 100)