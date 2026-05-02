# Write a program to build a home. The Home class should define all the attributes of each room in a home. From the Home class create two homes. FirstHome and SecondHome. First home should have an extra study room as a method. SecondHome should have the work_area as an extra method. should use the concept of inheritance.

class Home:
    def room1(self):
        width=100 
        breadth = 100 
        print("Area of room1:",width*breadth) 
    def kitchen(self):
        width = 1222
        breadth = 4888 
        print('are of kitchen',width*breadth)
    def hall(self):
        width = 200
        breadth = 150
        print("Area of hall:", width * breadth)

class FirstHome(Home):
    def study_room(self):
        width = 120
        breadth = 100
        print("Area of study room:", width * breadth)
class SecondHome(Home):
    def work_area(self):
        width = 140
        breadth = 110
        print("Area of work area:", width * breadth)

print("---- First Home ----")
home1 = FirstHome()
home1.room1()
home1.kitchen()
home1.hall()
home1.study_room()
print("\n---- Second Home ----")
home2 = SecondHome()
home2.room1()
home2.kitchen()
home2.hall()
home2.work_area()