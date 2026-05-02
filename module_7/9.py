# Write a program to create a copy of array and add an element to copied array . show both arrays.
# Program should accept an array from the user, swap the values of two arrays and display it on the console

arr1=[]
size1=int(input("Enter the size of the array: "))
print("Enter the values: ")
for i in range(size1):
    a1=int(input())
    arr1.append(a1)
arr2=arr1.copy()
size2=int(input("How many values you want to add: "))
print("Enter the values: ")
for i in range(size2):
    a2=int(input())
    arr2.append(a2)
arr1,arr2=arr2,arr1
print("arr1: ",arr1)
print("arr2: ",arr2)