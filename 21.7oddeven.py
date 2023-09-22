# user will give starting num and ending num and we have to print odd num
start = int(input("Enter a starting number: "))
end = int(input("Enter a ending number: "))
while start <= end:
    if (start % 2 == 0):
        # print("it's even")
        pass
    else:
        print("it's odd", start)
    start = start + 1