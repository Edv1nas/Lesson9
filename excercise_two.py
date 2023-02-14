# Find all number from 1-1000 that have 9 in them.

number_list = range(1,1000)

number_nine = [i for i in number_list if i % 10 == 9]

print(number_nine)