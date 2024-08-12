def prime_checker(number):
    if number <= 1:
        print(f"{number} is less than 1 or equal to 1 therefore it is not a prime")
    else:
        if number % 2 == 0:
            print(f"The {number} is not a prime number")
        elif number % 2 != 0:
            print(f"The {number} is a prime number")
        
n = int(input("Enter the number here: "))
prime_checker(number = n)       
    