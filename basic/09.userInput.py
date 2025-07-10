# py 09.userInput.py


user_input= input("Enter a number ")
if user_input.isdigit():
    num=int(user_input)
    print("You have entered a valid number:", num)
else:
    print("Invalid input!!")