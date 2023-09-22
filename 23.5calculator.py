#take 2 number and operators(+,-,/,*) if he choose + then + like that
num1 = int(input("Give a number: "))
num2 = int(input("Give a number: "))
choice = (input("enter your choice: "))
def sum(value1, value2):
    return value1+value2

def subtract(value1, value2):
    return value1-value2

def multiplication(value1, value2):
    return value1*value2

def divide(value1, value2):
    return value1/value2

def remainder(value1, value2):
    return value1%value2

if choice == "+":
    print(sum(num1, num2))
elif choice == "-":
    print(subtract(num1, num2))
elif choice == "*":
    print(multiplication(num1, num2))
elif choice == "/":
    print(divide(num1, num2))
elif choice == "%":
    print(remainder(num1, num2))
else:
    print("give correct input")
