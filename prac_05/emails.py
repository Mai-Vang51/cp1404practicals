"""
CP1404/CP5632 Practical
Emails
Estimate: 1 hour
Actual: 1 hour 10 minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = retrieve_name(email)
        confirmation = input(f"Is your name {name}? Y/n ").lower()
        if confirmation == "no" or confirmation == "n":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def retrieve_name(email):
    """Retrieve name from email"""
    email_component = email.split("@")
    email_prefix = email_component[0].split(".")
    name = " ".join(email_prefix).title()
    return name


main()
