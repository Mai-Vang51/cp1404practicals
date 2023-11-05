from guitar import Guitar


def load_guitars_list():
    guitars = []
    infile = open("guitars.csv", "r")
    for line in infile:
        parts = line.strip().split(",")
        guitars.append(Guitar(parts[0], parts[1], parts[2]))

    guitars.sort()
    for guitar in guitars:
        print(guitar)
    infile.close()


load_guitars_list()
