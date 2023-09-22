# straight triangle
i = 0
num = 5

while i <= num:
    j = 0
    while j < i:
        print("*", end = " ")
        j = j + 1
    print("\n")
    i = i + 1

# reverse triangle
i = 5
num = 0

while i >= num:
    j = 0
    while j <= i:
        print("*", end = " ")
        j = j + 1
    print("\n")
    i = i - 1