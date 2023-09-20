password = input("Password: ")
while len(password) < 8:
    print("Invalid. Need min of 8 characters.")
    password = input("Password: ")
print(len(password) * "*")
