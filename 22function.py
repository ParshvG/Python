def first_programme():
    print("my first function programme")


#brackets are imp to run the function if not the function will not run 
first_programme()

def full_name(name):
    print("full name", name)

full_name("parshv gandhi")

def complete_name(firstname, lastname):
    print("full name", firstname, lastname)

complete_name("parshv", "gandhi")

def addition(value, value1):
    print("sum", value + value1)

def addition(value1 ,value2, value3, value4):
    print("sum", value1, value2 + value3 + value4)

addition(1, 2, 3, 4)
addition(11, 22, 33, 44)

#inside brackets the values are called parameters or arguments
def multiplication(value, value1, value2):
    print("multiplication is", value * value1 * value2)

multiplication(1, 2, 3)
multiplication(1, 2, 4)
multiplication(1, 2, 5)