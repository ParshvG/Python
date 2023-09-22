# make two class make one class of parent and second class is of child only surname
class parent:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def my_surname(self):
        print("my surname is ", self.last_name)

class child(parent):
    pass

object = child("parshv", "gandhi")
object2 = parent("sharuk", "khan")
print(object.last_name)
print(object2.last_name)
object.my_surname()
object2.my_surname()