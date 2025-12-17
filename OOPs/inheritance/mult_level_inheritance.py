# class Car:
#     @staticmethod
#     def start():
#         print("car started..")
        
#     @staticmethod
#     def stop():
#         print("car stoped.")
        
        
# class ToyotaCar(Car):
#     def __init__(self,brand):
#             self.brand = brand
            
# class Fortuner(ToyotaCar):
#     def __init__(self,type ):
#         self.type = type
        
# car1 = Fortuner("diesel")
# car1.start()
            


#---------- Super method ---------------
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stoped...")

class Toyota:
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start

car1 = Toyota("priuse", "electric")
print(car1.type)
    
        

