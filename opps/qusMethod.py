# create  student class that takes name & subjects as arguments in constructor.
#Then create a method to print the average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.name = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
            print("hi", self.name, self.marks,"your ave score is :", sum/3)
        
        
s1 = Student("durgesh yadav",[89,67,45])
s1.get_avg()