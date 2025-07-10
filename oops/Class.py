# py Class.py

class Dog: #a class
    def __init__(self,name,breed): #constructor
        self.name=name
        self.breed=breed
    def bark(self):  #methods
        print(f"{self.name} of {self.breed} is barking..")   
    def sit(self):
        print(f"{self.name} is sitting")    
    def sell(self):
        print(f"{self.breed} is on sale, visit store")    

mydog= Dog("jacky", "labrador") #object
mydog2= Dog("tommy", "desi")

#calling methods
mydog.bark() 
mydog2.bark()
mydog.sit()
mydog2.sell()
print(mydog.name) #accessing attributes 