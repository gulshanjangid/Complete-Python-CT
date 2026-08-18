

# List Comprehension

# Basic syntax
# [expression for item in collection]
# numbers = [1, 2, 3, 4, 5]

# squares = []

# for num in numbers:
#     squares.append(num * num)
# squares = [num * num for num in  numbers]

# print(squares)




# names = ["gulshan", "rahul", "amit"]

# upper_names = [name.upper() for name in names]

# print(upper_names)

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [num for num in numbers if num % 2 == 0]

even_numbers = {num : num for num in numbers if num % 2 == 0}

print(even_numbers)


