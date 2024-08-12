print("This is a program to identify the word count")

text = input("Enter the sentence here: ")

words = text.split()

word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0)+1

for word, count in word_counts.items():
    print(f"{word}:{count}")