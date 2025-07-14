# py Poly.py
#polymorphism means many forms
# yani ek hi method ka alag-alag objects ke sath alag behavior

class Dog:
    def speak(self):
        return "HOOF!"
class Cat:
    def speak(self):
        return "meow"

# Yahan humne ek list banayi hai jisme Dog aur Cat ke objects hain
animals=[Dog(), Cat()]

for animal in animals:
    print(animal.speak())  # Polymorphism ka use yahan ho raha hai:
                           # animal object chahe Dog ho ya Cat,
                           # speak() method apne respective class ka output dega