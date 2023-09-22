tuple1 = (1, 10, "hi", "hello", 3.50)
#length
print(len(tuple1))
#type
print(type(tuple1))
#index
print(tuple1[2])
#range
print(tuple1[0:2])
#using in
if (10 in tuple1):
    print("yes")
else:
    print("no")
#converting tuple into list
list = list(tuple1)
list[0] = 1000
tuple1 = tuple(list)
print(tuple1)
#append
list = list(tuple1)
list.append(2)
tuple1 = tuple(list)
print(tuple1)
tuple2 = (2, 3, 4, "hi", "i am pg")
print(tuple1 + tuple2)
#delete tuple
del tuple1
print(tuple1)