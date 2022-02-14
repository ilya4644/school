from animals import *
p = Dog("Шарик", 5)
p.getting_older()
print(p.ages())
print(p.name())
#print(p.name(), ":", p.ages(), "лет")
pets = [Cat("Мурка", 3), p]
for p in pets:
    p.say()