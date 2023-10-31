"""
CP1404/CP5632 Practical
Programming Language
Estimate: 1 hr 30 minutes
Actual: 1 hr 15 minutes
"""

from programming_language import ProgrammingLanguage


def main():
    """Display format of programming languages in the print statement"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]
    display_dynamic_language(languages)


def display_dynamic_language(languages):
    """Print programming languages that are dynamically typed"""
    print(f"\nThe dynamically typed languages are: ")
    for language in languages:
        if language.is_dynamic():
            print(language.field)


main()
