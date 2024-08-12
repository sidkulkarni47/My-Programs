print("This is program for Palimdrome")

text = input("Enter the string here: ").lower()
my_list = []

for i in text:
    if i != ' ':
        my_list.append(i)
print(my_list)    

reversed_text = my_list[::-1]

print(reversed_text)

if my_list == reversed_text:
    print("The above text is a palimdrome!!!")
else:
    print("Not a Palimdrome!!!")