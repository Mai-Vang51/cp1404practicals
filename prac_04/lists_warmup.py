numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = 3, 1, 4, 1, 5, 9
# numbers[3:4] = 1, 5
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = False
# numbers + [6, 5, 3] = 3, 1, 4, 1, 5, 9, 2, 6, 5, 3

# 1.
new_value = "ten"
numbers[0] = new_value

# 2.
new_number = 1
numbers[-1] = new_number

# 3.
new_list = numbers[2:]
print(new_list)

# 4.
if 9 in numbers:
    print("True")
else:
    print("False")
