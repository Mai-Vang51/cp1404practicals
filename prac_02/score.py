"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    result = "Invalid Score"
elif score >= 90:
    result = "Excellent"
elif score >= 50:
    result = "Pass"
else:
    result = "Bad"
print(f"Your score is {result}")
