set1 = {"apple", "apple", "orange", 1, 2 , 50}
print(set1)
print(len(set1))
print("apple" in set1)
#add
set1.add("hi")
print(set1)
set1.remove("apple")
print(set1)
#union function
set2 = {"hi", 1, 2, 3}
print(set1.union(set2))
#update
set2.update(set1)
print(set2)