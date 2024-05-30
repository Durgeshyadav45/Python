class Student:
    def __init__(self, phy,chem, math) :
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def parcentage(self):
        return str ((self.phy + self.chem + self.math)/3)+"%"
    
stu1 = Student(98, 97 ,99)
print(stu1.parcentage)

stu1.phy = 86
print(stu1.parcentage)