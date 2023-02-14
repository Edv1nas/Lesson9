# Given string: text = 'In this lecture we will review some additional functionalities of python built-in data structures.' calculate how many words have letter 'e' in it.

text = "In this lecture we will review some additional functionalities of python built-in data structures."


count_e = [word for word in text.split() if  "e" in word]

print(len(count_e))
