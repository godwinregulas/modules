# Write a program to add to two dimensional arrays, understand the memory management of list 
# Program should accept two 2D arrays and display its sum

size=int(input("Enter the size of the array: "))
arr1=[]
print("Enter the values of array 1: ")
for i in range(size):
    lst=[]
    for j in range(size):
        a=int(input())
        lst.append(a)
    arr1.append(lst)

arr2=[]
print("Enter the values of array 2: ")
for i in range(size):
    lst=[]
    for j in range(size):
        a=int(input())
        lst.append(a)
    arr2.append(lst)

arr_sum=[]
for i in range(size):
    lst=[]
    for j in range(size):
        a=arr1[i][j]+arr2[i][j]
        lst.append(a)
    arr_sum.append(lst)
print("Sum of 2 arrays is:",arr_sum)