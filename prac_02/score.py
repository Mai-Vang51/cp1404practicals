"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid Score")

        score = float(input("Enter score: "))

    result = determine_grade(score)

    print(f"Your score is {result}")
    score = random.randint(0, 100)
    result = determine_grade(score)
    print(f"The score of {score} is a {result}")


def determine_grade(score):
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Pass"
    else:
        result = "Bad"
    return result


main()
