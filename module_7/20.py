# Write a program to include all the functionalities of a calculator using ABSTRACT class and abstract method. All the methods (add, sub, mul, div) should be inside of abstract class. Abstract method definition should be in another class

from abc import ABC,abstractmethod
class Calculator(ABC):
    @abstractmethod
    def add(self,a,b):
        pass
    @abstractmethod
    def sub(self,a,b):
        pass
    @abstractmethod
    def mul(self,a,b):
        pass
    @abstractmethod
    def div(self,a,b):
        pass
class CalcOper(Calculator):
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            print("cant divisible by 0, go to lp school")
        else:
            return a/b
obj=CalcOper()
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")
ch=int(input("Enter your choice: "))
a=float(input("Enter the first value: "))
b=float(input("Enter the second value: "))
if ch==1:
    print(obj.add(a,b))
elif ch==2:
    print(obj.sub(a,b))
elif ch==3:
    print(obj.mul(a,b))
elif ch==4:
    print(obj.div(a,b))
else:
    print("You have entered wrong choice, you fool!")