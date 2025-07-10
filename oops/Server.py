# py Server.py
#oops intro

class Server: #blueprint to create Server objects
 def __init__(self,name,ip):  #__init__ (double underscrore) :constructor method
     self.name=name
     self.ip=ip

 def status(self):
     print(f"{self.name} at {self.ip} is running...")

web_server= Server("jio server", "123.43.24.1") #instance of the class Server
web_server.status()