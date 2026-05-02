# Write a program to find the simple interest.
# Program should accept 3 inputs from the user and calculate simple interest for the given inputs. Formula: SI=(P*R*n)/100)

P=int(input("Enter the principal amount: "))
R=float(input("ENter the interest rate: "))
n=float(input("Enter the number of years: "))

SI=float((P*R*n)/100)
print("Simple interest (SI): "+str(SI))