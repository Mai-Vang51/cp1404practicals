"""
CP1404/CP5632 Practical
Colour code in dictionary
"""

COLOUR_TO_CODE = {"copper": "#b87333", "gray27": "#454545", "camel": "#c19a6b", "camouflagegreen": "#78866b",
                  "bananayellow": "#ffe135", "cedarchest": "#c95a49", "palevioletred4": "#8b475d",
                  "steelblue": "#4682b4", "straw": "#e4d96f", "viridian": "#40826d"}

print(COLOUR_TO_CODE)

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(f"{colour_name}: {COLOUR_TO_CODE[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()