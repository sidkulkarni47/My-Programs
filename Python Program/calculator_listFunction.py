print("Welcome to the calculator !!!")

operation = input("What mathematical operations would you like to perform! +, -, *, / : ")

n1 = int(input("Please enter the first number: "))
n2 = int(input("Please enter the second number: "))

def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

if operation == "+":
    result = add(n1,n2)
elif operation == "-":
    result = sub(n1,n2)
elif operation == "*":
    result = mul(n1,n2)
else:
    result = div(n1,n2)

print (result)