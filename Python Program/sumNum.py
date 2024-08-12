print("This is a program that we are writing to find a wheater 2 numbers in array add up to 57")

sum_input = int(input("Please enter the sum here: "))

array1 = [1, 2, 3, 4, 5]
array2 = [6, 7, 8, 9, 10]

found = False

for find1, find2 in zip(array1, array2):
    if find1 + find2 == sum_input:
        print("The sum of numbers is equal to the 2 numbers in the array! and numbers are ",find1, "and", find2)
        found = True

if not found:
    print("No two numbers in the arrays add up to the specified sum.")