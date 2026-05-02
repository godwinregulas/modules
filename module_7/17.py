# Write a menu driven program to do the basic mathematical operations such as addition, subtraction, 
# multiplication and division (hint: use if else ladder or switch)
# Program should have 4 functions named addition(), subtraction(), multiplication() and division()
# Should create a class object and call the appropriate function as user prefers in the main function

class math_op:
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        if b==0:
            print("Can not divisible by 0, you fool!")
        else:
            return a/b

obj=math_op()
print("1: Addition")
print("2: Subtraction")
print("3: multiplication")
print("4: division")
ch=int(input("Enter your choice: "))
a=float(input("Enter the first value: "))
b=float(input("Enter the second value: "))

match ch:
    case 1:
        print(obj.addition(a,b))
    case 2:
        print(obj.subtraction(a,b))
    case 3:
        print(obj.multiplication(a,b))
    case 4:
        print(obj.division(a,b))
    case _:
        print("you have entered wrong choice!")