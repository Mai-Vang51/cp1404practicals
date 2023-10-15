"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 1 hour
Actual: 
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? Y/n ").lower()


def extract_name_from_email(email):
    email_component = email.split("@")
    email_prefix = email_component[0].split(".")
    name = " ".join(email_prefix).title()
    return name


main()
