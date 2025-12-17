str1 = 'hellopython'  
str2 = "welcome to python"  #---use double quort to where using like 'python's tutorial' single qourt string stop 's
str3 = """python is most imprtent for backend"""

print(str1)

#----- Assign String to a Variable----
a = "Hello Coder"
print(a)


#---indexing---
str = "wellcome to the python"
print(str[5]) 


#--- Slicing -----
#Accessing part of a string
str = "Hello Python"
print(str[4:7])


#---Nagative Index----
str = "apple is a frutes"
print(str[-4: -1])


#----Multiple String-----?
a = """ You can assign a multiline,
        Srting to a variable by,
        Using three quotes,
        On three single quotes     
   """
print(a)


#---- Check String------
# To cheak if a charater is present in a string use the keyword in
str = "python is the most popular lanaguage"
print("most" in str)


#---- String  Functions-----
str = "I am a coder"
print(str.endswith("er")) #--- if returne er than true else false


#capitalize ---create new string 
str = "i am a coder"
str = str.capitalize()
print(str)


#old value change to new value orginal value can not change
str = "i am studing from online"
print(str.replace("o","a"))
print(str)


#---count Function---
str = "Hello i am from studing python from youtube"
print(str.count("o"))


#---combine string list without using loop(use join)
words = ["python", "is", "eass to learn"]
s = " ".join(words)
print(s) 



#Q1---Write a program to input user's name & print it's length----
name = input("Entenr user name")
print("length of your name", len(name))
