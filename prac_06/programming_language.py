"""CP1404/CP5632 Practical"""


class ProgrammingLanguage:
    def __init__(self, field="", typing="", reflection="", year=0):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.field}, {self.typing} Typing, Reflection:{self.reflection}, First appeared in " \
               f"{self.year}"

    def __repr__(self):
        return f"{self.field}, {self.typing}, {self.reflection}, {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"
