# local scope
def print_num(value):
    print(value)

print_num(3)

#global scope
x = "hi"
def num2(value):
    print(value)
    print(x)

num2(x)