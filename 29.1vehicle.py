#make class vehicle variable wheels company name speed model 
# declare one function move print my speed is use constructor
class vehicle:
    def __init__(self, wheel, companyname, model, speed):
        self.wheel = wheel
        self.companyname = companyname
        self.model = model
        self.speed = speed
    def move(self):
        print("my speed is")
    
vehicle = (4, "BMW", "X8", 120)
