# In multiple inheritance, a child class can inherit from more than one parent class.

# class A:
#     varA = "welcome to class A"
    
# class B:
#     varB = "welcome to  class B"
    
# class C(A, B):
#     varC = "welcome to class C"
    
# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)


class Person:
    def __init__(self, name):
        self.name = name
        
class Job:
    def __init__ (self, salary):
        self.salary = salary
        
class Employee(Person, Job):
    def __init__(self,name,salary):
        Person.__init__(self,name)
        Job.__init__(self, salary)
    
    def details(self):
        print("name",self.name,"Earns", self.salary)
        
emp = Employee("durgesh", 23000)
emp.details()
        
# Here Employee get attributes from both Person and job and it can access both name and salary