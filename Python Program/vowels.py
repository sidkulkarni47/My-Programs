print("Let's find the vowels in the word throught the program!!")

word = input("Please enter the words: ").lower()

vowels = ("a","e","i","o","u")

for find in vowels:
    if find in word:
        print("The vowels in the word is " + find)