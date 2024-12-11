#Task: Create a caluclator. Get user inputs and operation and outout the answer.

import art

#function to add the 2 numbers 
def add(n1, n2):
    return n1+n2

#function to subtract the 2 numbers 
def subtract(n1, n2):
    return n1-n2

#function to multiply the 2 numbers 
def multiply(n1, n2):
    return n1*n2

#function to divide the 2 numbers 
def divide(n1, n2):
    return n1/n2

def calculator():
    num1 = 0

    calculation = True
    while calculation:

        #get users first number
        if num1 == 0:
            print("\n"*100)
            print(art.logo)
            num1 = int(input("What is the first number? "))

        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")

        #get users next number
        num2 = int(input("What is the next number? "))

        #check operation and call the function for the operation
        result = 0
        if operation == "+":
            result = add(n1=num1, n2=num2)
        elif operation == "-":
            result = subtract(n1=num1, n2=num2)
        elif operation == "*":
            result = multiply(n1=num1, n2=num2)
        elif operation == "/":
            result = divide(n1=num1, n2=num2)
        else:
            print("ERROR! incorrect input")
        
        #print results
        print(f"{num1} {operation} {num2} = {result}")

        #Check if user wants to continue calculating with the result or start new
        continue_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calucation: ")
        
        if continue_calculation == "y":
            num1 = result
        elif continue_calculation == "n":
            num1 = 0
        else:
            print("Incorrect input!")
            num1 = 0

#call the calculator function to start
calculator()
