# squares = {i: i * i for i in range(10)}
# print(squares)

#Create a dictionary with 5 kay:value pairs, Keys must be strings, values must be numbers double digits(int)
# Use dictionary comprehension to create a new dictionary where keys are the same keys as your currents ones just all cappital letters, 
# and values are in reverse order. (25 -> 52)


# 1.

dic_n = {"raktas": 12, "puodukas":41, "batai":21, "kuprine":13, "miegmaisis":24}

new_dic = {key.upper(): int(str(val)[::-1]) for key, val in dic_n.items()}

print(new_dic)


# 2.

new_new_dic = {}

for key, val in dic_n:
    new_new_dic[key.upper()] = int(str(val)[::-1])

print(new_new_dic)
