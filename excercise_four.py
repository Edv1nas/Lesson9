# Given the same string as in previous exercise: calculate count of letters that have more than 5 characters.

text = "In this lecture we will review some additional functionalities of python built-in data structures."

count_e = [word for word in text.split() if len(word) >= 5]

print(len(count_e))