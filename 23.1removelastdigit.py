# in modules '%' we will get last digit
# in divide '/' it will remove last digit
num = int(input("enter a number: "))
while num > 0:
    print(num % 10)  # Get and print the last digit
    num = int(num / 10)  # Remove the last digit by integer division 