"""
CP1404/CP5632 Practical
Guitars
Estimate: 1 hr 30 minutes
Actual: 1 hr
"""

from guitar import Guitar

print("My guitars!")
guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{name} ({year})  : ${cost:,.2f} added.\n")
    name = input("Name: ")

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.get_age() >= 50 else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:,.2f} {vintage_string}")
