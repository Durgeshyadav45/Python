# --- if Satement-----

age = 24
#if age >= 18:
if (age >= 18):
    print("can vote")
    print("can drive") 
# if(True):
#     print("can vote")
#     print("can vote")

#-----elif-----
light = "yellow"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light =="yellow"):
    print("look")
else:
    print("light is broken")
    
print("end of code")


#-----else conditions-----
#all conditions all false in if statement then excute the else conditions

# num = 8
# if num % 2 == 0:
#     print("this number is even")
# else:
#     print("this number is odd")

#Q1--Grade student based on markes
    #    marks >= 90, grade = "A"
    #    90 > marks >= 80, grade = "B"
    #    80 > marks >= 70, grade = "C"
    #    70 > marks, grade = "D"
    
#marks = int(input("Enter student marks :"))
#marks = 73
"""if (marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >=70 and marks < 80 ):
    grade = "C"
else:
    grade = "D"

print("grade of student ->", grade)
"""



#----- Nesting if else statement --- ----
'''age = 82

if (age >= 18):
    if(age >= 80):  
      print("can not drive")
    else:
        print("can drive")
        
else:
    print("can not drive")'''
    
    
    
    
#Q2----Write a program to cheak if number entered by the user is odd or even.

# num = 9
'''num = int(input("enter the number: "))
if (num % 2 == 0):
    print("number is even")
else:
    print("number is odd") '''
    

#Q3--- Write a program to find the greatest of 3 numbers entered bu the user
'''a = int(input("enter frist number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if (a >= b and a >= c):
    print("frist number is largest", a)
elif(b >= c):
    print("second number is largest", b)
else:
    print("third number largest", c) '''   


#Q4 ---- WAP to chek if a number is multiple of 7 or not

#num = 27
num = int(input("Entetr a number"))

if (num % 7 == 0):
    print("multiple of 7")
    
else:
    print(" not a multiple")
    
