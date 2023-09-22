# user will give starting num and ending num and we have to print odd num
start = int(input("Enter a starting number: "))
end = int(input("Enter a ending number: "))
while start <= end:
    if (start % 4 == 0):
        print("it's a leap year", start)
    else:
        print("it's not a leap year", start)
    start = start + 1