#print string
print("1. Hello World!")

#string manipulation
print("2. Hello" + " World!")
print("3. Hello\nWorld!")
print('4. "Hello World!"')
print("5. \"Hello\" World!")

#inputs
print(input("6. What is your name? "))
print("7. Hello " + input("What is your name? "))

#Storing inputs in Variables
name = input("8. What is your name? ")
print("Hello "   + name)

#retrieving string length
print("9.")
print(len("Hello World!"))

#swapping value in variables
a = "a"
b = "b"

print("10. Swapping values in variables:")
print("a = " + a, "b = " + b)

print("Swap")
temp = b
b = a
b = temp

print("a = " + a, "b = " + b)