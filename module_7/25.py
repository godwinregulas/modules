# create a custom exception class and raise this exception when user press one in the menu and handles this exception

class MyException(Exception):
    pass

print("press 1 to raise the expeption")
ch=int(input())
try:
    if ch==1:
        raise MyException("You pressed 1 haha!")
except MyException as e:
    print("Exception caught",e)
else:
    print("Dont you know english?")