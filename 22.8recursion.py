def factorial(value):
    if value == 0:
        return 1
    

    return value* factorial(value - 1)
print(factorial(6))
# 6* factorial(6 - 1)
# 6* 5 * 4 * 3 * 2 * 1 = 720

def factorial(value):
    if value == 0:
        return 1
    

    return value+ factorial(value - 1)
print(factorial(6))
# 6+ factorial(6 - 1)
# 6+ 5 + 4 + 3 + 2 = 1 = 22