"""
CP1404/CP5632 Practical
Guitars
Estimate: 1 hr 30 minutes
Actual: 1 hr
"""

from guitar import Guitar

VINTAGE_AGE_THRESHOLD = 50


def main():
    """Get information about guitars and display if they are vintage"""
    print("My guitars!")
    guitars = get_guitar_info()
    display_dynamic_language(guitars)


def get_guitar_info():
    """Get guitar information from user"""
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{name} ({year})  : ${cost:,.2f} added.\n")
        name = input("Name: ")
    return guitars


def display_dynamic_language(guitars):
    """Print languages that are dynamically typed and are vintage"""
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.get_age() >= VINTAGE_AGE_THRESHOLD else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:,.2f} {vintage_string}")


main()
