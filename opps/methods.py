# methods are functions that belongs to objects

class Student:
    college_name ="kmclu"
    
    def __init__(self, name, marks):
        self.name = name
        self.name = marks
    
    def welcome(self):
        print("welcome student", self.name)
        
        
    def get_marks(self):
        return self.marks
        
        
s1 = Student("karan,", 97)
s1.welcome()
print(s1.get_marks,s1.name)