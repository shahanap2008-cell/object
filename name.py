class person:
    def __init__(self , name):
        self.name = name

    def greet(self):
        print("Hello my name is " + self.name)

p1 = person("Emil")
p1.greet()