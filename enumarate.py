

# values = ["a", "b", "c"]
# for index, value in enumerate(values):
#     print(index, value)


name_list = ["Tomas", "Linas", "Marius", "Tadas", "Karolis"]

name_dict = {index:name for index, name in enumerate(name_list, start=1)}

print(name_dict)

new_dict = {}

for index, name in enumerate(name_list, start=1):
    new_dict[index] = name

print(new_dict)

