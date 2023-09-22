#don't write direct divide by 2 put remainder will be 0 by 2 for odd and even function
number = int(input("ENTER A NUMBER: "))
if (number % 2) == 0:
    print("Number is even")
else:
    print("Number is odd")