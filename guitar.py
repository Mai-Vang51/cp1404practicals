"""CP1404/CP5632 Practical - Guitar"""

CURRENT_YEAR = 2023
VINTAGE_AGE_THRESHOLD = 50


class Guitar:
    """Represent guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise guitar object

        year: int, year of manufacture
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        """Return string of guitar object."""
        return f"{self.name} ({self.year}): ${self.cost}"

    def get_age(self):
        """Calculate age of guitar by taking year of manufacture from previous year."""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Determine if guitar object is vintage if older than 50 years."""
        return self.get_age() > VINTAGE_AGE_THRESHOLD

    def __lt__(self, other):
        """Determine if the guitar object year is later than other guitar object year."""
        return self.year < other.year
