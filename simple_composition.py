class Dog:

    def bark(self):
        print("Woof!")
    
class Robot:

    def move(self):
        print("Moving...")

class Robot_cleaner:

    def clean(self):
        print("Claning...")

class Superbot:

    def __init__(self):
        
        self.object1 = Dog()
        self.object2 = Robot()
        self.object3 = Robot_cleaner()

    def move(self):
        return self.object2.move()
    
    def bark(self):
        return self.object1.bark()
    
    def clean(self):
        return self.object3.clean()

jacob = Superbot()
jacob.bark()
        


