#creating  class
class Student:
    
    def __init__(self,name, marks,age):
        self.name=name
        self.marks = marks
        self.age = age
        print("adding new student in database")
  
#object              
s1 = Student("durgesh", 89, 18)
print(s1.name,s1.marks,s1.age)

s2 = Student("amit", 67, 23)
print(s2.name,s2.marks, s2.age)
        
    

