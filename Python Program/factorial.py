print("This is a program to tell us the factorial of the number!!!")

num = int(input('Enter the number here: '))
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i
    print(factorial)
print(f"The end factorial is- ", factorial)