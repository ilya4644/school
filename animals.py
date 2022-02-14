class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
    def getting_older(self):
        self.age += 1
    def name(self):
        print(self.name)
    def ages(self):
        print(self.age)
class Cat(Pet):
    def say(self):
        print("Мяу")

class Dog(Pet):
    def say(self):
        print("Гав")