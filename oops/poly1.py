# py poly1.py
#example of abstraction and polymorphism together
import math

class Shape:
    def area(self):
       pass #abstract 
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi * self.radius ** 2
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return  self.side ** 2

# Ab polymorphism ka use: Shapes naam ka list banaya 
#jisme alag-alag objects hain (Circle aur Square)
Shapes = [Circle(5), Square(8)]  # Dono Shape type ke hain, par behavior alag hai

for Shape in Shapes:
    print(f"Area: {Shape.area()}")

#Abstraction ka matlab hai base class me sirf method declare karna,
# implement nahi karna (Shape class me area() method).

#Polymorphism ka matlab hai ek hi method naam (area()) hone ke bawajood,
# alag-alag classes me uska behavior alag ho (Circle me aur Square me alag area calculation).