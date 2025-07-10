# py 06.Loop.py

for i in range(1,6):
    print(f"checking server {i}")
  


#WHILE LOOP
server_up=False
while not server_up:
    print("Waiting for the server to start")
    server_up=True #block k andr wala chij m --same line se start kro
print("Server is running and Up!")  #ye block k bhar tha
