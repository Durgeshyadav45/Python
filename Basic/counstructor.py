# Class and Objects

class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"name:{self.name}, age:{self.age}")
        
# create a object     
s1 = Student("durgesh", 23)
s1.show()



   