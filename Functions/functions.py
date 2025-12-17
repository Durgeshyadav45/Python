#------ Create a function--------
def my_function():
    print("welcome to the python")
    
#------ Calling the functions------

def my_function():
    print("welcome to the python")

my_function()
# function multiple time
my_function()



#------ why use function------------
#because of you would have to write the same code repeatedly

#----without function------ Ex:-  convert temperature
# temp1 = 44
# celsius1 = (temp1 - 22) * 5/9
# print(celsius1)

# temp2 = 23
# celsius2 = (temp2 -11) *5/9
# print(celsius2) 



#---- Write a function to print length of list.

cities = ["Noida", "Kanapur", "Lucknow", "Delhi", "Gurgaun", "Pune"]
books = ["Hindi", "English", "Maths", "Chemistry","physics","cumputer"]

def city(list):
    print(len(list))

city(cities)

#-----list in a single line-----
def city(list):
    for items in list:
        print(items, end=" ") #--using end =" " list in a single line
city(books)


#Q2---write a program to find the factorial of n
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    
factorial(5)


#-----convert USD TO INR------
def convert(usd_val):
    inr_val = usd_val * 90
    print(usd_val, "USD", inr_val,"INR")
    
convert(72)



     

        

