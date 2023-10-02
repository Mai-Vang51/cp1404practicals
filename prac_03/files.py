"""
CP1404/CP5632 - Practical
Answer the following questions:
1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
   Remember to close your file.
2. (In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the name
   (as above) then prints, "Your name is Bob" (or whatever the name is in the file).
3. Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on
   separate lines in the file and save it:
   17
   42
   400
   Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result,
   which should be... 59.
4. Now write a fourth block of code that prints the total for all lines in numbers.txt or
   a file with any number of numbers.
"""

# 1.
# name = input("Name: ")
# with open("name.txt", "w") as outfile:
#     print(f"{name}", file=outfile)
#
# 2.
# FILENAME = "name.txt"
# in_file = open("name.txt")
# name = in_file.read()
# in_file.close()
# print(f"Your name is {name}")

# 3.
# in_file = open("numbers.txt")
# first_number = in_file.readline()
# second_number = in_file.readline()
# print(int(first_number) + int(second_number))
# in_file.close()

# 4.
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
    print(total, file=in_file)
