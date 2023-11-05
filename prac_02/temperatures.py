"""
CP1404 - Practical 2
"""

MENU = """C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            temperature = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {temperature:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            temperature = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {temperature:.1f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
