# py Animal.py

#parent class
class Animal:
    def __init__ (self,name,):
        self.name=name
    def speak(self):
        print(f"{self.name} is making noise!")

#child classes        
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof!")
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow!")
class Tiger(Animal):
    def speak(self):
        print(f"{self.name} says roar!!")        



dog1=Dog("Jacky")
cat1=Cat("kitty")
tiger1=Tiger("Shera")

dog1.speak()
cat1.speak()
tiger1.speak()


