"""CP1404/CP5632 Practical - Guitar"""

CURRENT_YEAR = 2022
VINTAGE_AGE_THRESHOLD = 50


class Guitar:
    """Represent guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise guitar object

        year: int, year of manufacture
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        """Return string of guitar object"""
        return f"{self.name} ({self.year}): {self.cost}"

    def get_age(self):
        """Calculate age of guitar by taking year of manufacture from previous year"""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Return True for guitar is vintage if object is older than 50 years"""
        return self.get_age() > VINTAGE_AGE_THRESHOLD

    def __lt__(self, other):
        """Determine the latest guitar by year to other guitar object"""
        return self.year < other.year
