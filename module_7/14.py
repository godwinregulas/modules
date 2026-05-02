# Write a program using user defined functions and lambda functions

def intro(name,age,place):
    print(name)
    print(age)
    print(place)

add=lambda a,b: a+b

intro("Godwin Regulas",30,"Kochi")
print("--------------------------")
print("Sum:",add(5,10))