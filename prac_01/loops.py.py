for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0, 110, 10):
    print(i, end=" ")
print()

# b.
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# c.
number_of_star = int(input("Number of stars: "))
for i in range(number_of_star):
    print("*", end="")
print()

# d.
number_of_star = int(input("Number of stars: "))
for i in range(1, number_of_star + 1):
    print(i * "*")

