"""
CP1404/CP5632 Practical
Programming Language
Estimate: 1 hr 30 minutes
Actual: 1 hr 15 minutes
"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programming_languages = [python, ruby, visual_basic]
print(programming_languages)

print(f"The dynamically typed languages are: ")
for language in programming_languages:
    if language.is_dynamic():
        print(language.field)
