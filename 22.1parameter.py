#it's imp to call the function in any case otherwise it will not work
def addition(value = 3, value1 = 5):
    print("sum", value + value1)

addition()

def addition1(value = 3, value1 = 5):
    print("sum", value + value1)

addition1(10, 10)

#multiple parameter
#star is for infinite value we can add in call function
def multiple_parameter(*value):
    print(value[0])
multiple_parameter(1, 2, 3)

def multiple_parameter1(value1, *value):
    print(value)
    print(value1)
multiple_parameter1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)