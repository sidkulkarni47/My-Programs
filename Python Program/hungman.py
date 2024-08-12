import random

print("Welcome to the Hangman Game!!!")

word_list = ["ardvark","baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()



for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("wrong")

print(f'Pssst, the solution is {chosen_word}')

display = []

for letter in chosen_word:
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()