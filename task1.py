# py task1.py

input_n1=input("Enter the first number")
input_n2=input("Enter the second number")
if input_n1.isdigit() and input_n2.isdigit():
    num1=int(input_n1) #int bna do
    num2=int(input_n2)  #int bna do
else:
    print("Enter the valid number")
    exit()   #exit the program

input_s=input("Enter the operator")
if(input_s=="*"):
    cal=num1*num2
elif(input_s=="+"):
    cal=num1+num2
elif(input_s=="-"):
    cal=num1-num2
elif(input_s=="/"):
    cal=num1/num2
elif(input_s=="%"):
    cal=num1%num2
else:
   print("Invalid operator")
   exit()

print("Result: ", cal)