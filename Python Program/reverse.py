print('This is a program to reverse the spring!!')

input_str = input("Enter the string you want to reverse: ")

str_list = []

for i in input_str:
    if i != '':
        str_list.append(i)
      
str_list.reverse()

print(str_list)