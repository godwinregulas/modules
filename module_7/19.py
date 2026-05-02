#  Write a program to add the values of two 2D arrays
# Program should contain a class, Functions should be inside the class

class array:
    def getArray(self):
        self.arr1=[]
        self.arr2=[]
        self.arr_sum=[]
        self.n=int(input("Enter the size of the array: "))
        print("Enter the values of array1: ")
        for i in range(self.n):
            lst=[]
            for j in range(self.n):
                a=int(input())
                lst.append(a)
            self.arr1.append(lst)

        print("Enter the values of array2: ")
        for i in range(self.n):
            lst=[]
            for j in range(self.n):
                a=int(input())
                lst.append(a)
            self.arr2.append(lst)

    def addArray(self):
        for i in range(self.n):
            lst=[]
            for j in range(self.n):
                a = self.arr1[i][j] + self.arr2[i][j]
                lst.append(a)
            self.arr_sum.append(lst)

    def displayArray(self):
        print("Sum of the 2 arrays:",self.arr_sum)

obj=array()
obj.getArray()
obj.addArray()
obj.displayArray()