"""
CP1404/CP5632 Practical
My Guitars
Estimate: 1 hr 30 minutes
Actual: 1 hr 50 minutes
"""

from guitar import Guitar


def main():
    """Get and update guitar lists into file"""
    guitars = load_guitars_list()

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Name: ")

    guitars.sort()
    for guitar in guitars:
        print(guitar)
    save_current_list(guitars)


def load_guitars_list():
    """Load guitar lists from file"""
    guitars = []
    infile = open("guitars.csv", "r")
    for line in infile:
        parts = line.strip().split(",")
        guitars.append(Guitar(parts[0], int(parts[1]), parts[2]))
    infile.close()
    return guitars


def save_current_list(guitars):
    """Save updated list to file"""
    outfile = open("guitars.csv", "w")
    for guitar in guitars:
        print(f"{guitar.name}, {guitar.year}, {guitar.cost}", file=outfile)
    outfile.close()


main()
