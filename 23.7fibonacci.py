num1 = 0
num2 = 1
sum = 0

while sum < 25:
    num1 = num2
    num2 = sum
    sum = sum + num1
    print(sum)