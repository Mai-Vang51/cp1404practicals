"""
CP1404/CP5632 Practical
Do-from-scratch Exercise
"""
import random

NUMBER_OF_NUMBERS_NEEDED = 6
MINIMUM_GENERATING_NUMBER = 1
MAXIMUM_GENERATING_NUMBER = 45

number_of_picks = int(input("How many quick picks? "))
for line in range(number_of_picks):
    chosen_numbers = []
    for number in range(NUMBER_OF_NUMBERS_NEEDED):
        generated_number = random.randint(MINIMUM_GENERATING_NUMBER, MAXIMUM_GENERATING_NUMBER)
        while generated_number in chosen_numbers:
            generated_number = random.randint(MINIMUM_GENERATING_NUMBER, MAXIMUM_GENERATING_NUMBER)
        chosen_numbers.append(generated_number)
    chosen_numbers.sort()
    for number in chosen_numbers:
        print(f"{number:2}", end=" ")
    print()
