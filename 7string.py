#this is multiline string
multiline_name='''This,
is
string
'''
print(multiline_name)
name="parshv gandhi"
print(name)
#build-in function
print(len(name))
#finding word in paragraph
print("parshv" in name)
print("abc" not in name)
#index
print(name[-1])
#range index
print(name[0:])
#for caps
print(name.upper())
#for small
print(name.lower())

name2="parshv gandhi"
name3=name2.split("a")
hello=name2.replace("par","   hello   ")
print(name3)
print(hello)
removespace = "        hi        "
print(len(removespace))
print(len(removespace.strip()))
hi=hello.strip()
print("my name is", hi)
name4="parshv"
name5="gandhi"
name6=name4 +" "+ name5
print(name6)

age=18
textvariable="my name is Parshv,my age is {}"
print(textvariable.format(age))

print("my name is Parshv,my age is", age)
full_name="\"parshv gandhi\""
print(full_name)