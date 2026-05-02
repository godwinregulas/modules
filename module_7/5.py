# Write a program to show the grade obtained by a student after he/she enters their total mark percentage.
# Program should accept an input from the user and display their grade as follows

marks=float(input("Enter your mark percentage: "))

if marks>90:
    print("Grade: A")
elif marks>=80 and marks<=89:
    print("Grade: B")
elif marks>=70 and marks<=79:
    print("Grade: C")
elif marks>=60 and marks<=69:
    print("Grade: D")
elif marks>=50 and marks<=59:
    print("Grade: E")
elif marks<50:
    print("Failed!")
else:
    print("You have entered wrong mark percentage!")