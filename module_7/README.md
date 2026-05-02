# Visit this link for all the questions. If it's not working, you can rely on text given below
# https://docs.google.com/document/d/1IJSi2NZPT0b-341dArukR32vZfcFj4CmuHa6p1pmY78/edit?usp=sharing


Assignments 

Accept a char input from the user and display it on the console.
Code of the program & screenshot of the output.
Accept two inputs from the user and output its sum.

Variable
Data Type
Number 1
Integer
Number 2
Float
Sum
Float



Code of the program & screenshot of the output.
Write a program to find the simple interest.
Program should accept 3 inputs from the user and calculate simple interest for the given inputs. Formula: SI=(P*R*n)/100)
Variable
Data Type
Principal amount (P)
Integer
Interest rate (R)
Float
Number of years (n)
Float
Simple Interest (SI)
Float



Code of the program & screenshot of the output.
Write a program to check whether a student has passed or failed in a subject after he or she enters their mark (pass mark for a subject is 50 out of 100).
Program should accept an input from the user and output a message as “Passed” or “Failed”
Variable 
Data type
mark
float



Code of the program & screenshot of the output.
 Write a program to show the grade obtained by a student after he/she enters their total mark percentage.
Program should accept an input from the user and display their grade as follows
Mark
Grade
> 90
A
80-89
B
70-79
C
60-69
D
50-59
E
< 50
Failed


Variable 
Data type
Total mark
float



Code of the program & screenshot of the output.
Using the ‘switch case’ write a program to accept an input number from the user and output the day as follows. 

Input
Output
1
Sunday
2
Monday
3
Tuesday
4
Wednesday
5
Thursday
6
Friday
7
Saturday
Any other input
Invalid Entry



Code of the program & screenshot of the output.
Write a program to print the multiplication table of given numbers. Using for and while
Accept an input from the user and display its multiplication table
Eg: 
Output: Enter a number
Input: 5
Output: 
1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
4 x 5 = 20
5 x 5 = 25
6 x 5 = 30
7 x 5 = 35
8 x 5 = 40
9 x 5 = 45
10 x 5 = 50
Code of the program & screenshot of the output.
Write a program to print the following pattern (hint: use nested loop)
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


Code of the program & screenshot of the output.
Write a program to create a copy of array and add an element to copied array . show both arrays.
Program should accept an array from the user, swap the values of two arrays and display it on the console
Eg: Output: Enter the size of Array 1
Input: 5
Output: Enter the values of Array 1
Array 1: 10, 20, 30, 40, 50
Array 2 : Copy of Array 1
Array 2 : 10, 20, 30, 40, 50 + add a element
Output :   Array 1 [10, 20, 30, 40, 50 ]
Output :  Array 2 [10, 20, 30, 40, 50, 60, 70  ]



Code of the program & screenshot of the output.
 Write a program to sort an array in descending order without sort() and sorted() Program should accept and array, sort the array values in descending order and display it
Selection
Insertion
bubble

      Eg: Output: Enter the size of an array
Input: 5
Output: Enter the values of array
Input: 20, 10, 50, 30, 40
Output: Sorted array:
50, 40, 30, 20, 10
Code of the program & screenshot of the output.
Write a program to identify whether a string is a palindrome or not without using reverse(), slicing
A string is a palindrome if it reads the same backward or forward eg: MALAYALAM
Program should accept a string and display whether the string is a palindrome or not
Eg: Output: Enter a string
Input: MALAYALAM
Output: Entered string is a palindrome
Eg 2: Output: Enter a string
Input: HELLO
Output: Entered string is not a palindrome
Code of the program & screenshot of the output.
Write a program to add to two dimensional arrays, understand the memory management of list 
Program should accept two 2D arrays and display its sum
Eg: Output: Enter the size of arrays
Input: 3
Output: Enter the values of array 1
Input: 
1 2 3
4 5 6
7 8 9
Output: Enter the values of array 2
Input:
10 20 30
40 50 60
70 80 90
Output: Sum of 2 arrays is:
11 22 33
44 55 66
77 88 99
Code of the program & screenshot of the output.
Grades are computed using a weighted average. Suppose that the written test counts 70%,  lab exams 20% and assignments 10%.
If Arun has a score of
Written test = 81
Lab exams = 68
Assignments = 92
Arun’s overall grade = (81x70)/100 + (68x20)/100 + (92x10)/100 = 79.5
 Write a program to find the grade of a student during his academic year. 
Program should accept the scores for written test, lab exams and assignments
Output the grade of a student (using weighted average)
Eg:
Enter the marks scored by the students
Written test = 55
Lab exams = 73
Assignments = 87
Grade of the student is 61.8
Code of the program & screenshot of the output
Study about functions 
User defined
Types of Arguments
Lambda
      Write a program using user defined functions and lambda functions
          Code of the program & screenshot of the output
  Write a program to accept an array and display it on the console using functions
Program should contain 3 functions including main() function
main()
Declare an array
Call function getArray()
Call function displayArray()
		getArray()
Get values to the array
		displayArray()
Display the array values
Study about global, local, non-local
Code of the program & screenshot of the output.
Write a program to print “HELLO WORLD “using function without using print inside of function. (“HELLO WORLD “must be inside Decorator function) 
Code of the program & screenshot of the output.
 Write a menu driven program to do the basic mathematical operations such as addition, subtraction, multiplication and division (hint: use if else ladder or switch)
Program should have 4 functions named addition(), subtraction(), multiplication() and division()
Should create a class object and call the appropriate function as user prefers in the main function
Code of the program & screenshot of the output.
Write a program to print the following pattern using for loop
7 8 9 10 
4 5 6
2 3
1
Code of the program & screenshot of the output.
 Write a program to add the values of two 2D arrays
Program should contain a class, Functions should be inside the class
Call function getArray() using an object
Call function addArray() using an object
Call function displayArray() using an object
		getArray()
Get values to the array
		getArray()
Add array 1 and array 2
		displayArray()
Display the array values

Eg:
Enter the size of array
2
Enter the values of array 1
1	2
3	4
Enter the values of array 2
5	6
7	8
Output:
Sum of array 1 and array 2:
6	8
10	12
Code of the program & screenshot of the output
Write a program to include all the functionalities of a calculator using ABSTRACT class and abstract method. All the methods (add, sub, mul, div) should be inside of abstract class. Abstract method definition should be in another class. 

Examples : 
from abc import ABC, abstractmethod
 class Calculator(ABC): 
         def __init__(self, id, name): 
              self.id = id self.name = name
        @abstractmethod 
        def add (self): 
                   pass
Code of the program & screenshot of the output
Write a program to build a home. The Home class should define all the attributes of each room in a home. From the Home class create two homes. FirstHome and SecondHome. First home should have an extra study room as a method. SecondHome should have the work_area as an extra method. should use the concept of inheritance.
class Home:
     def __init__(self):
          pass 
    def room1: 
         width=100 
         breadth = 100 
         print('are of room1',width*breath) 
   def kitchen: 
          width = 1222
         breadth = 4888 
         print('are of kitchen',width*breath) 
         you should have mentioned all the plans of home here as methods. 

Class FirstHome(Home): 
         # define the extra method's
                   pass 
class SecondHome(Home): 
         # define the extra method's 
                  pass
Code of the program & screenshot of the output
Write a program to create Class with name and account number and implement get and set, with property decorator and making account number and name private.  
Write a function to calculate the sum of all numbers passed as its arguments. Your function should be called sum_numbers and should define a single variable             argument (i.e. a star argument) that will get the values to sum.

      Test the function with the following values:

Values                Result
1, 2, 3                      6
8, 20, 2                    30
12.5, 3.147, 98.1    113.747
             1.1, 2.2, 5.5           8.8
pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes = {
    "Butter chicken": [
        "chicken",
              "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}


observe the dictionary above and write a menu driven python program to create recipes. Once one recipe is done then the quantity of the items in pantry should also be reduced
Eg  :  If you cook beans on toast the beans quantity and bread quantity need to decrease i.e., one from the total quantity each.
create a custom exception class and raise this exception when user press one in the menu and handles this exception. 
Write a list comprehension that returns the list ["1*2=1", "22=4", "32=9", ...., "25*2=625"]
Using dict comprehension and a conditional argument create a dictionary from the current dictionary where only the key:value pairs with value above 2000 will be taken to the new dictionary.
dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2={}

