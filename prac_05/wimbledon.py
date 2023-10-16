"""
CP1404/CP5632 Practical
Wimbledon
Estimate: 1 hour 45 minutes
Actual: 2 hour 15 minutes
"""

def main():
    names = []
    name_to_count = {}
    countries = []
    with open("wimbledon.csv", "r", encoding="utf-8_sig") as in_file:
        in_file.readline()
        for line in in_file:
            annual_tournament = line.strip()
            records = list(annual_tournament.split(","))
            country = records[1]
            countries.append(country)
            name = records[2]
            names.append(name)
        for name in names:
            try:
                name_to_count[name] += 1
            except KeyError:
                name_to_count[name] = 1

        print("Wimbledon Champions:")
        for name, count in name_to_count.items():
            print(f"{name} {count}")
        print()

        champion_country = sorted(set(countries))
        print(", ".join(champion_country))


main()