# Write a program to identify whether a string is a palindrome or not without using reverse(), slicing

data=str(input("Enter a string: "))
start=0
end=len(data)-1
is_true=1
while start<end:
    if data[start]!=data[end]:
        is_true=0
        break
    start+=1
    end-=1

if is_true==1:
    print("It's palindrome!")
else:
    print("It's not palindrome!")