#for return function we have to store call function in variable compulsory if you use return
def addition(value, value1):
    return value + value1

sum = addition(1, 2)
print(sum)

def multiplication(value, value1):
    return value * value1

multiply = multiplication(1, 2)
print(multiply)

# mathod 2 if you don't want to make variable then direct print
def division(value, value1):
    return value / value1

print(division(1, 2))

#in function their will be only one return pls don't add to many return 
def div(value, value1):
    return value / value1
    return 0

print(div(300, 200))
