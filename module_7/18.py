num=7
x=4
for i in range(1,5):
    for j in range(x):
        print(num, end=" ")
        num+=1
    num=num-x-(x-1)
    x=x-1
    print()