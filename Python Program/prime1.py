print("Prime number program!")

num = int(input("Enter the ending number till you need an list of prime number: "))

start = 2


for start in range(start, num + 1):
    if start % 2 != 0 :
        if start % 3 != 0:
            print(start)
     