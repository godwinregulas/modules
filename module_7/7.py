# Write a program to print the multiplication table of given numbers. Using for and while
# Accept an input from the user and display its multiplication table

num=int(input("Enter a number: "))

for i in range(1,11):
    print(i, "x", num, "=", i*num)