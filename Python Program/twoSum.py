print("Program to add 2")

my_list = []

for i in range (4):
    listEntry = int(input("Enter the number here: "))
    my_list.append(listEntry)
print(my_list)

for i in range (len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] + my_list[j] == 9:
            print(i,j)
