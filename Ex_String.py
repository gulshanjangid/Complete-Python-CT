# s = "Hello gulshan"



# # print(s[::])
# print(s[:])
# # print(s[7:])

# # print(s[:6]) 

# # print(s[-11:-1]) 
# # print(s[-1])

# # print(s[::-1])
# # print(s[::])



# # #Empty string
# # s = ""
# # print(s[::0])


# Here’s a clear and complete guide to string slicing in Python with examples and edge case handling.

# Basic Syntax
# Pythonsubstring = string[start:end:step]


# start → index where the slice begins (inclusive, default 0)
# end → index where the slice ends (exclusive, default len(string))
# step → interval between characters (default 1)


# Examples
# Python# Example string
# text = "Hello  Gulshan"
# print(text[20:2])
# # 1. Basic slicing
# print(text[0:6])     # 'Python'  → characters from index 0 to 5
# print(text[7:])      # 'Programming' → from index 7 to end
# print(text[:6])      # 'Python' → from start to index 5

# # 2. Using step
# print(text[0:6:2])   # 'Pto' → every 2nd character from index 0 to 5

# # 3. Negative indices
# print(text[-11:-1])  # 'Programmin' → count from the end (-1 is last char)
# print(text[-1])      # 'g' → last character

# # 4. Reverse string
# print(text[::-1])    # 'gnimmargorP nohtyP'

# # 5. Partial reverse
# print(text[6::-1])   # ' nohtyP' → reverse from index 6 to start



# empty = ""
# print(empty[:])  # ''

# # Step cannot be zero
# try:
#     print(text[::0])
# except ValueError as e:
#     print("Error:", e)  # step argument must not be zero

# # Start > End with positive step → returns empty string
# print(text[5:2])  # ''






text = "apple apple apple"

print(text.replace("apple", "mango", 3))