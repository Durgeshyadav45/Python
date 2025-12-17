# create a class and object
# class is blueprint for creating object

#creating class
class Student:
    name = "sumit kumar"  #---parametar
    
#creating object(is instanse of class)
s1 = Student()
print(s1.name) 


#-----__init__ Function-----(__init__ is a Constructors)
class Student:
    def __init__(self,name, marks):  #self is parametar
        self.name = name
        self.marks = marks
        print("adding new student in database..")
        
s1 = Student("amit", 98)
print(s1.name, s1.marks)


#----Methods-------
# Methods are functions that belong to object
class Student:
    def __init__(self,name, marks):  #self is parametar
        self.name = name
        self.marks = marks
    #methods----(insite a class's functions)
    def welcome(self):
        print("wecome to student", self.name)
        
    def get_marks(self):
        return self.marks
        
 #object----       
s1 = Student("amit", 98)
s1.welcome()
print(s1.get_marks())


#Q1--- Create student class that name & marks of 3 subjects as agruments in constructor.
       # Then create a method to print the average
       
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hello", self.name, "your avg score is:", sum/3)
        
s1 = Student("durgesh",[78, 56, 63])
s1.avg()
        
        
#change value 
s1.name = "sumit"
s1.avg()
