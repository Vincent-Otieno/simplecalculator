# Ask for first number
a = float(input("First number: "))

# Ask for the math sign
op = input("Choose +, -, * or / : ")

# Ask for second number
b = float(input("Second number: "))

# Do the math
if op == "+":
    print(a + b)

elif op == "-":
    print(a - b)

elif op == "*":
    print(a * b)

elif op == "/":
    print(a / b)
    
else:
    print("Wrong sign!")