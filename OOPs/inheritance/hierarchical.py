# multiple child classes inherit from the same parent class

#In This Example two child classes(Emp and intern) inheriting from a single parent class Person
class Person:
    def __init__(self, name):
        self.name = name
        
class Employee(Person):
    def role(self):
        print(self.name,"working as an employee")
        
class Intern(Person):
    def role(self):
        print(self.name,"is an intern")
        
emp = Employee("durgesh")
emp.role()

intern = Intern("sumit")
intern.role()

#Explanation: Both Employee and Intern inherit from Person.
#They share the parent’s property (name) but implement their own methods.