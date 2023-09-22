#take 2 number and operators(+,-,/,*) if he choose + then + like that
num1 = int(input("Give a number: "))
num2 = int(input("Give a number: "))
choice = (input("enter your choice: "))

if choice == "+":
    print(num1 + num2)
elif choice == "-":
    print(num1 - num2)
elif choice == "*":
    print(num1 * num2)
elif choice == "/":
    print(num1 / num2)
elif choice == "%":
    print(num1 % num2)
else:
    print("give correct input")
