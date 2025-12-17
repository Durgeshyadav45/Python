# methods are functions that belongs to objects
#class Method

# class Student:
#     college_name ="kmclu"
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.name = marks
    
#     def welcome(self):
#         print("welcome student", self.name)
        
        
#     def get_marks(self):
#         return self.marks
        
        
# s1 = Student("karan,", 97)
# s1.welcome()
# print(s1.get_marks,s1.name)


#-----------Static Methods------------
#Methods that don't use the self parametar(and this is work at class level not Object level)
#Static method can't access or modify class state and generally for utility
class Student:
    stdCount = 0 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.stdCount += 1
    
    @staticmethod  #------decorater ---->Decorators allow us to wrap another function in order                                 
    def showcount():             #-- to extend the behaviour of the wrapped function, without permanently modifying it 
        print(Student.stdCount)
            
        
s1 = Student("karan,", 23)
s2 = Student("sumit", 26)
print("number of student: ")
Student.showcount()
print(s1.name, s1.age)


#------ Class Methods----------
# A class method is bound to the class and receives the class as an implicit frist agrument
class Person:
    name = "anonymous"
    age = 23
    marks = 44.5
    
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("aditya yadav")
print(p1.name, p1.marks)


