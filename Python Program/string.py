print("This program is to count number of alphabets without repeating")

input_str = input("Enter the string that you want to check: ").lower()

str_list = []
new_list = []

for i in input_str:
    if i != ' ':
        str_list.append(i)
print(str_list)

for j in (len(str_list)):
    for k in range(j+1,len(str_list)):
        if str_list[j] != str_list[k]:
            new_list.append(str_list[j])
print(new_list)

# recheck error!!!