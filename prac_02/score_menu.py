MENU = """(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"""


def main():
    print(MENU)
    valid_score = get_valid_score()
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            valid_score = get_valid_score()
        elif choice == "P":
            print(determine_grade(valid_score))
        elif choice == "S":
            print_stars(valid_score)
        else:
            print("Invalid choice")

        print(MENU)
        choice = input("Choice: ").upper()
    print("Farewell")


def get_valid_score():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def determine_grade(valid_score):
    if valid_score >= 90:
        result = "Excellent"
    elif valid_score >= 50:
        result = "Pass"
    else:
        result = "Bad"
    return result


def print_stars(valid_score):
    print("*" * valid_score)


main()
