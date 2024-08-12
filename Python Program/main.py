num = int(input("How many numbers do you want int the list? - "))

list = []
new_list = []
zero_list = []

for a in range (num + 1):

    input_list = int(input("Enter the numbers into the list: "))

    list.append(input_list)

print(list)

for i in list:
    if i != 0:
        new_list.append(i)
    elif i == 0:
        zero_list.append(i)
    
print(new_list)
print(zero_list)

combined_list = new_list + zero_list

print(combined_list)