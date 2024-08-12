print("This is a program to find whether the number is prime or not.")

num = int(input("Please enter the number here: "))

if num < 1: 
    print(num,"is not a prime number")
    for i in range(2,num):
        if num % i == 0:
            print(num, "is a prime number")
        else:
            print(num, "not a prime number")