# class fan:
#     def on(self):
#         print("fan is on")

# dl = fan()   # object
# dl.on()


# class tv:
#     def watch(self):
#         print("i am watching tv")

# dl = tv()
# dl.watch()


class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

p1 = person("emil",36)

print(p1.name)
print(p1.age)
