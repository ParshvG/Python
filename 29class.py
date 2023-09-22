class student:
    rollnumber = 10
    name = "parshv"
    grade = 90
    gender = "male"
    
object1 = student()
parshv = student()
print(object1.rollnumber)

class person:
        count = 0
        def __init__(self, name, age):
              self.name = name
              self.age = age
              person.count += 1
              print("my name is", self.name, "my age is", self.age)
        def my_name(self):
               print("my age is", self.age)

person1 = person("parshv", 18)
person2 = person("john", 25)
print(person.count)
person1.my_name()
person2.my_name()
person1.age = 17
person1.my_name()
del person1
person1.name 