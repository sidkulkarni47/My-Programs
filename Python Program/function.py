print("Welcome to the calculator!!!")

number_1 = int(input("Please enter the number one: "))
number_2 = int(input("Please enter the number two: "))

choice = int(input("Please enter 1.Add, 2.Sub, 3.Mult, 4.Div"))


def addition():
    add = number_1 + number_2
    print(f"The addition of the numbers is {add}")

def subtraction():
    sub = number_1 - number_2
    print(f"The subtraction of the numbers is {sub}")

def multiplication():
    mult = number_1 * number_2
    print(f"The multiplication of the numbers is {mult}")

def division():
    div = number_1 / number_2
    print(f"The division of the numbers is {div}")

if choice == 1:
    addition()

elif choice == 2:
    subtraction()

elif choice == 3:
    multiplication()

else:
    division()