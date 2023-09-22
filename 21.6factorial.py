#multiply in it i can't be 0 so answer will be 0 and tu understand mistake run i and multiply with together like this print("i ", i, "multiply", multiply)
num = int(input("enter a number: "))
i = num
multiply = 1
while i >= 1:
    multiply = multiply * i
    i = i - 1
print(multiply)