"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    total = get_total_income(incomes, number_of_months)
    print_income_report(incomes, number_of_months, total)


def get_total_income(incomes, number_of_months):
    total_income = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total_income += income
    return total_income


def print_income_report(incomes, number_of_months, total):
    print("\nIncome Report\n-------------")
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        print(f"Month {month:2} - Income: ${income:10.2f}           Total: ${total:10.2f}")


main()
