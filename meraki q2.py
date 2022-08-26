# Now you have to solve some questions by using the pre-define function.
# Q1 . You have to print the largest value out of the given list using the max function.
# Input
# Code Example
numbers = [3, 5, 7, 34, 2, 89, 2, 5]
Output :-
89
def max():
    a=[3,5,7,34,2,89,2,5]
    i=0
    max=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        i=i+1
    print(max)
max()