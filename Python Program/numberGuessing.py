import random

print("This is a number guessing game!!!")

# Generate the computer's random number
def computer():
    return random.randint(1, 100)

computer_num = computer()

for _ in range(1, 10 + 1):
    num = int(input("Guess a number and enter it: "))

    if computer_num < num:
        print("The number is low! Guess another one.")
    elif computer_num > num:
        print("The number is high! Guess another one.")
    else:
        print("Congratulations! You guessed the correct number.")
        break  # Exit the loop if the number is guessed

    if _ == 10:
        print(f"Sorry, you've reached the maximum number of attempts. The correct number was {computer_num}.")