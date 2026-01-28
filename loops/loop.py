#--------- For Loop-------
# n = 5
# for i in range(0, n):
#     print(i)

#----- For Loop with String-----
# s = "python"
# for i in s:
#   print(i) 


#Print number from 1 to 100
'''i = 1
while i <= 100: #----this is stopring conditions
    print(i)
    i += 1'''
    
#Q2- Print number from 100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i -=1
    

#Q3- print the multiplication table of number n
# n = int(input("Enter Number :"))
'''i = 1
while i <= 10:
    print(n*i)
    i += 1'''
    

#Q4- Print the elements of the following list using a loop
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1'''
    
#Q5:- WAP to find of frist n numbers(using While loop)
n = 5

sum = 0
i = 0
while i <= n:
    sum += 1
    i += 1
print("total sum =", sum)


#----While loop Example------
Pass = 12345
user_input = ""

while user_input != Pass:
    
    user_input = int(input("Enter password:"))
    if user_input != Pass:
        print("Invalid passwoed")
        
print("Login Successfull")

#----- FOR LOOP-------
#--- Other Examples---- with break 
'''i = 0
while i <= 5:
    if (i == 3):
        print("Found item.." ,i)
        break
    i +=1'''
    
#---- For Loop ---- 
'''tup = [1,2,3, 5,6, 7]
for num in tup:
    print(num)
    
nums = [1, 4, 6, 9, 16, 25, 36, 49]
for element in nums:
    print(element)'''

#----Range Functions-----
'''for i in range(1,10):
    print(i)
    '''
#rever number
'''for i in range(10, 0, -1):
    print(i)
    '''
    
n = 5

