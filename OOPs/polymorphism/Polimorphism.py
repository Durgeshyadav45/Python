class Bird():
    def sound(self):
        print("Bird's make sound")
        
class Crow(Bird):
    def sound(self):
        print("Crows say cow caw")
        
class Parrot(Bird):
    def sound(self):
        print("parrot sound squawk")
        
bird1 = Crow()
bird2 = Parrot()

bird1.sound()
bird2.sound()