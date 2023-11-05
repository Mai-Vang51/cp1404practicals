MENU = """(H)ello
(G)oodbye
(Q)uit"""

customer_name = input("Enter Name: ")
print(MENU)
choice = input().upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {customer_name}")
    elif choice == "G":
        print(f"Goodbye {customer_name}")
    else:
        print("Invalid choice")

    print(MENU)
    choice = input().upper()

print("Finished.")
