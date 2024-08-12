print("This is a program to calculate the sum of nested array!")

nested_array = [[1, 2, 3], [4, 5], [6, [7, 8, 9], 10], [11, [12, [13, 14]]]]

add = 0

for num in nested_array:
    for num1 in num:
        if isinstance(num1, int):
            add = add + num1
print("This sum",add)