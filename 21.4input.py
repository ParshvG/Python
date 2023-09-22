#take user input number and loop to that number 
i = int(input("starting number: "))
num = int(input("enter a number: "))
gap = int(input("enter a gap you want: "))
while i <= num:
    print(i)
    i = i + gap
# ending number should be greater than starting no and gap should be positive else show an error
i = int(input("starting number: "))
num = int(input("enter a number: "))
gap = int(input("enter a gap you want: "))
if (num > i and gap > 0):
    while i <= num:
        print(i)
        i = i + gap
else:
    print("error it's negative")
