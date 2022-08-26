
# e a function named add_numbers which takes two numbers as arguments and then prints their sum. The name of the arguments should be number1 and number2.

# Input :-


# Code Example
# # Write add_numbers function here
# num1 = 56
# num2 = 12
# add_numbers(num1,num2)

# Output :-
# 68
# Question (Part 2)
# Write a function named add_numbers_list which takes 2 lists of two integers and then prints the sum of the integers with the same position.

# Use the add_numbers function given in Part 1 to count 2 integers that have the same position.

# If we give [50, 60, 10] and [10, 20, 13] to this function it will print this

# 60
# 80
# 23
# 1
def add(num1,num2):
    print(num1+num2)
add(56,12)
# 2
def sum():
    a= [50, 60, 10] 
    b=[10, 20, 13]
    d=[]
    i=0
    while i<len(a):
        c=a[i]+b[i]
        d.append(c)
        i=i+1
    print(d)
sum()