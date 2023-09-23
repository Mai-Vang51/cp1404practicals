"""
CP1404 - Practical 2
"""

MIN_LENGTH = 8


def main():
    password = get_password()
    print_asterisk_password(password)


def get_password():
    password = input("Password: ")
    while len(password) < MIN_LENGTH:
        print("Invalid. Need min of 8 characters.")
        password = input("Password: ")
    return password


def print_asterisk_password(password):
    print(len(password) * "*")


main()
