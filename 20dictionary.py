fullname={
    "first name":"parshv",
    "last name":"gandhi",
    "age": 18,
    "age": 17,
}
print(fullname)
# we will define no index
print(fullname["first name"])
fullname["first name"] = "parshv1"
print(fullname)
print(fullname["age"])
print(fullname.keys())
print(fullname.values())
#adding new items
fullname["hobby"] = ["cricket", "basketball", "football", "enginner"]
print(fullname)
fullname["address"] = {"area": "ahmedabad", "pincode": 380013 }
print(fullname)
#for removing
fullname.pop("address")
print(fullname)
#delete function
del fullname["hobby"]
print(fullname)
#clear function
fullname.clear()
print(fullname)
#delete function
del fullname
print(fullname)
