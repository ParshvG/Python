# class name will animal leg,tail,colour,sound add function speak i speak and sound
# second class human first_name, age, lanuage add function speak i speak and lanuage
class animal:
    def __init__(self, leg, tail, colour, sound):
        self.leg = leg
        self.tail = tail
        self.colour = colour
        self.sound = sound

    def speak(self):
        print("i speak", self.sound)

class human:
    def __init__(self, first_name, age, lanuage):
        self.first_name = first_name
        self.age = age
        self.lanuage = lanuage

    def speak(self):
        print("i speak", self.lanuage)

object = human("parshv", "18", "gujarati")
object2 = animal("4", "1", "black", "baw-baw")
object.speak()
object2.speak()