print('This is a program to check whether the words are anagram or not!')

input1 = input("Enter the first word: ").lower()
input2 = input("Enter the second word: ").lower()
Input1WordList = []
Input2WordList = []

if len(input1) == len(input2):
    print("Length is same")
    for i in input1:
        Input1WordList.append(i)
    for j in input2:
        Input2WordList.append(j)
    Input1WordList.sort()
    Input2WordList.sort()
    if Input1WordList == Input2WordList:
        print("The inputs are similar!, and the words are anagram")
else:
    print("Not a Anagram")        

