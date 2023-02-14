# squares = []
# for number in range(10):
#     squares.append(number * i)
# print(squares)

# squares =[number * number for number in range(10) if range ==5]
# print(f" second:squares")

# name_list = ["Tomas", "Linas", "Marius", "Tadas", "Karolis"]

# longest_name = max(name_list, key=len)

# print(longest_name)


# 1. 

name_list = ["Tomas", "Linas", "Marius", "Tadas", "Karolis"]

new_list = []


for name in name_list:
    if len(name)>= 5:
        new_list.append(name)

print(new_list)


name_comp = [name for name in name_list if len(name)>=5]
print(name_comp)


