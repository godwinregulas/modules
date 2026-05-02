# Write a program to print “HELLO WORLD “using function without using print inside of function. (“HELLO WORLD “must be inside Decorator function) 

def decorator(func):
    def wrapper():
        func()
        return "HELLO WORLD"
    return wrapper

@decorator
def say_hello():
    pass

print(say_hello())