"""
CP1404/CP5632 Practical
Wimbledon
Estimate: 1 hour 45 minutes
Actual: 3 hour 15 minutes
"""


def main():
    records = read_file()
    name_to_count, countries = process_records(records)
    print_data(countries, name_to_count)


def read_file():
    """Read each line in file"""
    with open("wimbledon.csv", "r", encoding="utf-8_sig") as in_file:
        in_file.readline()  # Read and ignore first line
        return [lines.strip().split(',') for lines in in_file.readlines()]


def process_records(records):
    """Retrieve name of champions with their country and number of games won"""
    name_to_count = {}
    names = [record[2] for record in records]
    countries = [record[1] for record in records]
    for name in names:
        try:
            name_to_count[name] += 1
        except KeyError:
            name_to_count[name] = 1
    return name_to_count, countries


def print_data(countries, name_to_count):
    """Print champion name, games won, and country"""
    for name, count in name_to_count.items():
        print(name, count)
    print()
    print(", ".join(sorted(set(countries))))  # sort countries alphabetically and print as a single string


main()
