#  Now we debug the code related to function.
# Question 1
# Code Example
#  greet(names):
#      for name in names:
#   print("Welcome", name)
# gredefet("Rinki", "Vishal", "Kartik", "Bijender")
# # solve debug
def greet(*names):
    for name in names:
     print("Welcome", (name))
greet("Rinki", "Vishal", "Kartik", "Bijender")
# Question 2
# Code Example
# def info(name, age = ):
#    print(name + " is " + age + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18")

# Question 3


# Code Example

# def studentDetails(name,currentMilestone,mentorName):
#  print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)


# studentDetails("Nilam","loop")
def studentdetails(name,c,mentor):
    print("Hellow",name,"your",c,"concept","is clear with the help of ","mentorname")
studentdetails("nilam",)