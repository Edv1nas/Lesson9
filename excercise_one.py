# Find all of the numbers from 1-1000 that are divisible by 6.

number_list = range(1,1000)

divided_numbers = [i for i in number_list if not i %6]

print(divided_numbers)
