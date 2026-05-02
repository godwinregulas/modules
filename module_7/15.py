# Write a program to accept an array and display it on the console using functions
# Program should contain 3 functions including main() function

def main():
    arr=[]
    getArray(arr)
    displayArray(arr)

def getArray(arr):
    n=int(input("enter the size of the array: "))
    print("Enter the values: ")
    for i in range(n):
        a=input()
        arr.append(a)

def displayArray(arr):
    print("array values:",arr)

main()