def main():
    password = get_password()
    print_asterisk_password(password)


def get_password():
    password = input("Password: ")
    while len(password) < 8:
        print("Invalid. Need min of 8 characters.")
        password = input("Password: ")
    return password


def print_asterisk_password(password):
    print(len(password) * "*")


main()
