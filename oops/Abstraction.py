#py Abstraction.py


from abc import ABC,abstractmethod  # Abstraction ke liye ABC module import kiya jaata hai
 #abstact base class (abc)

class Car(ABC):
    @abstractmethod  
    def start_engine(self):  #ye ek abstract method hai , yha srf declare hoga, define nhi!
        pass
class Tesla(Car):
    def start_engine(self):
        print ("Tesla is starting silently..")
class Tata(Car):
    def start_engine(self):
        print("Tata is starting....")


my_car=Tesla()
my_car.start_engine()  
my_car2=Tata()
my_car2.start_engine()              


#Car class sirf ek blueprint hai — 
#isme bataya gaya hai ki har car ko start_engine() method zaroor rakhna chahiye.
##Lekin kaise start hoga, wo detail Tesla aur Tata classes deti hain.
#Ye hi hota hai abstraction — base class mein sirf idea hota hai, detail subclasses mein hoti hai.