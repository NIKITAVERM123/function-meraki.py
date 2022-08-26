# Use the min function and find the minimun va 
# Code Example
list = [8, 6, 4, 8, 4, 50, 2, 7]
Output :-
2 
def min():
  a = [8, 6, 4, 8, 4, 50, 2, 7]
  i=0
  min=a[0]
  while i<len(a):
    if (a[i])<min:
        min=(a[i])
    i=i+1
  print(min)
min()


 