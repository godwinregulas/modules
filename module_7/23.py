# Write a function to calculate the sum of all numbers passed as its arguments. Your function should be called sum_numbers and should define a single variable             argument (i.e. a star argument) that will get the values to sum.

def sum_numbers(*num):
    result=0
    for i in num:
        result+=i
    return result

print(sum_numbers(1, 2, 3 ))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))