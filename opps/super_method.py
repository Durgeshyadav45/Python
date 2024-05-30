class Car:
    def __init__(self, type):
        self.type = type
        
        
    @staticmethod 
    def start():
        print("car started.")
        
    @staticmethod 
    def stop():
        print("car stop.")
        
        
class ToyotaCar(Car):
    def __init__(self,name,type):
            super().__init__(type)
            self.name = name
            
car1 = ToyotaCar("priuse", "electric")
print(car1.type)
