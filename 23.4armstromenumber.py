num = int(input("enter a number: "))
sum = 0
temp = num

def cube(value):
    return (value ** 3)

while temp > 0:
    last_digit = temp % 10
    cube_of_number = cube(last_digit)
    sum = sum + cube_of_number
    temp = temp // 10

if (sum == num):
    print(num ," is armstrome number")
else:
    print(num ," is not a armstrome number")