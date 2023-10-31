"""CP1404/CP5632 Practical - Programming Language"""


class ProgrammingLanguage:
    """Represent a programming language object"""

    def __init__(self, field="", typing="", reflection="", year=0):
        """Initialise programming language object"""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string of programming language object"""
        return f"{self.field}, {self.typing} Typing, Reflection:{self.reflection}, First appeared in " \
               f"{self.year}"

    def is_dynamic(self):
        """Return True or False if programming language is dynamic"""
        return self.typing == "Dynamic"
