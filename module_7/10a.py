n=int(input("Enter the size the array: "))
arr=[]
print("Enter the values: ")
for i in range(n):
    a=int(input())
    arr.append(a)
for i in range(n):
    max_index=i
    for j in range(i+1, n):
        if arr[max_index]<arr[j]:
            arr[max_index],arr[j]=arr[j],arr[max_index]

print("Sorted array: ",arr)