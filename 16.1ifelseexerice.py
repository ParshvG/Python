#Finding small value
x=int(input ("enter a number1 "))
y=int(input ("enter a number2 "))
z=int(input ("enter a number3 "))
if (x <= y and x <= z):
    print("small value", x)
elif (y <= x and y <= z):
    print("small value", y)
elif (z <= y and z <= x):
    print("small value", z)
else:
    print("enter valid input")