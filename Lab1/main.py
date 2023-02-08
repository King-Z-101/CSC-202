class Flower:

    # Common base class for all Flowers
    def __init__(self, petalName, petalNumber, petalPrice):
     self.name = petalName
     self.petals = petalNumber
     self.price = petalPrice

    def setName(self, petalName):
     self.name = petalName

    def setPetals(self, petalNumber):
     self.petals = petalNumber

    def setPrice(self, petalPrice):
     self.price = petalPrice

    def getName(self):
     return self.name

    def getPetals(self):
     return self.petals

    def getPrice(self):
     return self.price


# This would create first object of Flower class

f1 = Flower("Sunflower", 2, 1000)

print("Flower Details:")
print("Name: ", f1.getName())
print("Number of petals:", f1.getPetals())
print("Price:", f1.getPrice())
print("\n")

# This would create second object of Flower class

f2 = Flower("Rose", 5, 2000)
f2.setPrice(3333)
f2.setPetals(6)

print("Flower Details:")
print("Name: ", f2.getName())
print("Number of petals:", f2.getPetals())
print("Price:", f2.getPrice())


# Output:

# Flower Details:
# Name:  Sunflower
# Number of petals: 2
# Price: 1000
#
#
# Flower Details:
# Name:  Rose
# Number of petals: 6
# Price: 3333



