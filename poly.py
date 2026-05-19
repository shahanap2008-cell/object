class car:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

    def move(self):
        print("drive!")

class boat:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

    def move(self):
        print("sail!")

class plane:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

    def move(self):
        print("fly!")

car1 = car("ford" , "mustang")
boat1 = boat("ibiza" , "touring 20")
plane1 = plane("boeing" , "747")

for x in (car1 , boat1 , plane1):
    x.move()