# numbers = {10, 20, 20, 30, 10}

# print(numbers)
# print(numbers[0])  #TypeError: 'set' object is not subscriptable

# Because sets are unordered collections and don't support normal indexing.

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)    #Combines two sets

print(a & b)   #common values.
print(a - b)
