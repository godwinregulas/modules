# Write a program to create Class with name and account number and implement get and set,
# with property decorator and making account number and name private.

class BankAccount:
    def __init__(self,name,acc_no):
        self.__name=name
        self.__acc_no=acc_no
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
    @property
    def acc_no(self):
        return self.__acc_no
    @acc_no.setter
    def acc_no(self,acc_no):
        self.__acc_no=acc_no

obj=BankAccount("Godwin Regulas",789456123)
print(obj.name)
print(obj.acc_no)
obj.name="Josu Damodaran"
obj.acc_no=94567823
print(obj.name)
print(obj.acc_no)