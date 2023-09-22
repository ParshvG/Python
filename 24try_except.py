# if we get error and programme is not running and you want to run the programme so we can use try except and run the programme
num1 = 10
num2 = "hi"
try:
    print(num1 / num2)
except ZeroDivisionError:
    print("you can't divide by zero")
except:
    print("error occured")
finally:
    print("finally")
print("programmes continue")

num1 = 10
num2 = 9
if num2 == 0:
    raise Exception("you can't divide by zero")
print(num1 / num2)