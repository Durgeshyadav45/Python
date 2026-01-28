#----file read-- Basic File Reading-- 
'''f = open("./file handling/demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()'''

#find specific characters in file
'''f = open("./file handling/demo.txt","r")
data = f.read(46)
print(data)
print(type(data))
f.close()'''
 
#-----Using With Keyword----- r mode

# with open("./file handling/demo.txt", "r") as f:
#     data = f.read()
#     print(type( data))

#---- w Write mode ----
# with open("./file handling/demo.txt", "w") as f:
#     f.write("welcome to the python and \n how to use it")

 
#----Delete a File-----
# import os
# os.remove("./file handling/demo.txt")

#----Prictice Questions-----
'''Create a file "prictice.txt" 
Hi everyone
we are learing File I/O
using java
I like programing in java
'''
# WFA that replace occurrences of "java" with "python" in above file
#Search if the word "learning" exits in the file or not


# with open ("./file handling/prictice.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("Java", "Python")
# print(new_data)
    
# with open("./file handling/prictice.txt","w") as f:
#     f.write(new_data)

#Search if the word "learning" exits in the file or not
'''def check_for_word():
    word = "learning"   
    with open("./file handling/prictice.txt ", "r") as f:
      data = f.read()
      if ( word in data):
         print("Found")
      else:
         print("Not Found")       
check_for_word()'''



#---- From a file containing number separated by comma, print the count of even
#---(mumber is like this 3,4,6,7,8,9,75,27,89,67 in the file)---

count = 0
with open ("./file handling/num.txt", "r") as f:
    data = f.read()
    
    nums = data.split(",")
    for item in nums:
        if (int(item) % 2 == 0):
            count += 1
    print(count)
      

    
   
 