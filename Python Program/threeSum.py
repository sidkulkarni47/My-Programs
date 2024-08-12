print("This is a program to calculate the numbers in array that gives 0")

my_list = []

for i in range(5):
    input_list = int(input("Enter the numbers in here: "))
    my_list.append(input_list)
print(my_list)

for i in range(len(my_list)):
    for j in range(i+1, len(my_list)):
        for k in range(j+1, len(my_list)):
            if my_list[i] + my_list[j] + my_list[k] == 0:
                print(i, j, k)