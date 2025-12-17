# set is automatacally remove duplicate value

num = {2, 4, 5, 3, 4, 5, 6, 6}
print(num)



class Car:
    color = "blue"
    brand = "mercedes"
    
car1 = Car()
print(car1.color)
print(car1.brand)

class Student:
    def __init__(self,name):
        self.name = name
        print("adding new student in data")
        
s1 = Student("shivam")
print(s1.name)

s2 = Student("aditya")
print(s1.name)
