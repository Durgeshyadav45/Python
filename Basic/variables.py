# -----Variables------

age  = 23  
name = "durgesh" 
old = True
a = None
print(type(name))
print(name)

#--- Dynamic Type ----
x = 10
print(type(x)) #--- x is integer

x = "durgesh"
print(type(x)) #-- x is now string

x = [2, 4, 5]
print(type(x)) # -- x is now list

# ----  Print Sum  ----
a = 1000
b = 500
sum = a+b
print(sum)

name = "Durgeshyadav"
length = len(name)
print("length of world", length)



# -----Input and Output-----
# name = input("enter your name")
# print("welcome", name)

'''int("5")
val = int(input("Enter your val"))
print(type(val),val)''' #int 23, 3.5 and value in str 

"""name = input("enter your name")
age = int(input("enter age:"))
marks = float(input("enter marks"))

print("welcome:", name)
print("age =", age)
print("marks =", marks)
"""

#----Question-----
# -- (1) Write a program to input 2 number & print their sum

"""a = int(input("enter frist value"))
b = int(input("enter second value"))
print ( "sum =", a + b)"""

# --(2) Write a program to input side of a square & print its area
"""side = float(input("enter square side:"))
print("area = ", side ** 2)

"""
#--(3) WAP to input 2 floting point numbers & print their average.
"""a = float(input("enter frist number"))
b = float(input("enter second number"))
print("avg =", (a+b)/2)"""

#--(4)WAP to input 2 int numbers a and b. Print True if a is greater than >= or equal to b. 
# If not print False
a = int(input("enter frist number"))
b = int(input("enter second number"))
print (a >=b)

