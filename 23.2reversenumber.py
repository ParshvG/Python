num = int(input("enter a number: "))
reverse = 0
while num > 0:
    last_digit = (num % 10)
    reverse = (reverse * 10) + last_digit 
    num = (int(num / 10))
print("reverse is", reverse)