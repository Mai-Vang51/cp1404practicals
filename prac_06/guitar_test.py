"""
CP1404/CP5632 Practical
Guitar Test
Estimate: 1 hr 30 minutes
Actual: 1 hr
"""

from guitar import Guitar


def run_test():
    """Test get_age and is_vintage method"""
    guitar = Guitar("Gibson L-5 CES", 1922)
    another_guitar = Guitar("Another guitar", 2013)
    age = guitar.get_age()
    another_age = another_guitar.get_age()
    print(f"{guitar.name} get_age() - Expected 100. Got {age}")
    print(f"{another_guitar.name} get_age - Expected 9 Got {another_age}")
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage - Expected False. Got {another_guitar.is_vintage()}")

    old_guitar = Guitar("old guitar", 1972)
    old_age = old_guitar.get_age()
    print(f"{old_age} {old_guitar.name} is_vintage() - Expected True. Got {old_guitar.is_vintage()}")


run_test()
