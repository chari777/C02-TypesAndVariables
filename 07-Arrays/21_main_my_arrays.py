###
# Program korzystający z modułu MyArrays
#
import MyArrays

numbers = [7, 3, 8, 5, 2]

print('Numbers:', MyArrays.to_string(numbers).replace('-', ','))
print('Second largest number:', MyArrays.second_largest(numbers))
print('Median:', MyArrays.median(numbers))
smallest, largest = MyArrays.min_max(numbers)
print(f'Smallest and largest number: {smallest},{largest}')
print('Numbers as a string:', MyArrays.to_string(numbers))
print('Max - min difference:', MyArrays.max_min_difference(numbers))
