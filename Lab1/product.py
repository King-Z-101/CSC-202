class Product:
    #Common base class for all Products
    def __init__(self, productName, productAmmount, productPrice):
        self.name = productName
        self.amount = productAmmount
        self.price = productPrice

    def get_price(self, itemsBought):
        total = 0
        if itemsBought < 10:
            total = itemsBought * self.price
        elif 10 <= itemsBought < 99:
            total = itemsBought * self.price * 0.9
        else:
            total = itemsBought * self.price * 0.8

        return total

    def make_purchase(self, itemsBought):
        if self.amount > itemsBought:
            self.amount = self.amount - itemsBought
            return self.amount
        else:
            raise ValueError('We only have {} {}!', self.amount, self.name)


class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit.strip().lower()

    measurement = 0

    def inches(self):
        if (self.unit == "feet"):
            measurement = self.length * 12
        if (self.unit == "yards"):
            measurement = self.length * 36
        if (self.unit == "miles"):
            measurement = self.length * 5280 * 12
        if (self.unit == "kilometers"):
            measurement = self.length * 39370
        if (self.unit == "meters"):
            measurement = self.length * 39.37
        if (self.unit == "centimeters"):
            measurement = self.length / 2.54
        if (self.unit == "millimeters"):
            measurement = self.length / 25.4
        elif (self.unit == "inches"):
            measurement = self.length

        return round(measurement, 2)

    def feet(self):
        if (self.unit == "inches"):
            measurement = self.length / 12
        if (self.unit == "yards"):
            measurement = self.length * 3
        if (self.unit == "miles"):
            measurement = self.length * 5280
        if (self.unit == "kilometers"):
            measurement = self.length * 3281
        if (self.unit == "meters"):
            measurement = self.length * 3.281
        if (self.unit == "centimeters"):
            measurement = self.length / 30.48
        if (self.unit == "millimeters"):
            measurement = self.length / 304.8
        elif (self.unit == "feet"):
            measurement = self.length

        return round(measurement, 2)

    def yards(self):
        if (self.unit == "inches"):
            measurement = self.length / 36
        if (self.unit == "feet"):
            measurement = self.length / 3
        if (self.unit == "miles"):
            measurement = self.length * 1760
        if (self.unit == "kilometers"):
            measurement = self.length * 1094
        if (self.unit == "meters"):
            measurement = self.length * 1.094
        if (self.unit == "centimeters"):
            measurement = self.length / 91.44
        if (self.unit == "millimeters"):
            measurement = self.length / 914.4
        elif (self.unit == "yards"):
            measurement = self.length

        return round(measurement, 2)

    def miles(self):
        if (self.unit == "inches"):
            measurement = self.length / 63360
        if (self.unit == "feet"):
            measurement = self.length / 5280
        if (self.unit == "yards"):
            measurement = self.length / 1760
        if (self.unit == "kilometers"):
            measurement = self.length / 1.609
        if (self.unit == "meters"):
            measurement = self.length / 1609
        if (self.unit == "centimeters"):
            measurement = self.length / 160900
        if (self.unit == "millimeters"):
            measurement = self.length / 1609000
        elif (self.unit == "miles"):
            measurement = self.length

        return round(measurement, 2)

    def kilometers(self):
        if (self.unit == "inches"):
            measurement = self.length / 39370
        if (self.unit == "feet"):
            measurement = self.length / 3281
        if (self.unit == "yards"):
            measurement = self.length / 1094
        if (self.unit == "miles"):
            measurement = self.length * 1.609
        if (self.unit == "meters"):
            measurement = self.length / 1000
        if (self.unit == "centimeters"):
            measurement = self.length / 100000
        if (self.unit == "millimeters"):
            measurement = self.length / 1000000
        elif (self.unit == "kilometers"):
            measurement = self.length

        return round(measurement, 2)

    def meters(self):
        if (self.unit == "inches"):
            measurement = self.length / 39.37
        if (self.unit == "feet"):
            measurement = self.length / 3.281
        if (self.unit == "yards"):
            measurement = self.length / 1.094
        if (self.unit == "miles"):
            measurement = self.length * 1609
        if (self.unit == "kilometers"):
            measurement = self.length * 1000
        if (self.unit == "centimeters"):
            measurement = self.length / 100
        if (self.unit == "millimeters"):
            measurement = self.length / 1000
        elif (self.unit == "meters"):
            measurement = self.length

        return round(measurement, 2)

    def centimeters(self):
        if (self.unit == "inches"):
            measurement = self.length * 2.54
        if (self.unit == "feet"):
            measurement = self.length * 30.48
        if (self.unit == "yards"):
            measurement = self.length * 91.44
        if (self.unit == "miles"):
            measurement = self.length * 160934
        if (self.unit == "kilometers"):
            measurement = self.length * 100000
        if (self.unit == "meters"):
            measurement = self.length * 100
        if (self.unit == "millimeters"):
            measurement = self.length / 10
        elif (self.unit == "centimeters"):
            measurement = self.length

        return round(measurement, 2)

    def millimeters(self):
        if (self.unit == "inches"):
            measurement = self.length * 25.4
        if (self.unit == "feet"):
            measurement = self.length * 304.8
        if (self.unit == "yards"):
            measurement = self.length * 914.4
        if (self.unit == "miles"):
            measurement = self.length * 1609340
        if (self.unit == "kilometers"):
            measurement = self.length * 1000000
        if (self.unit == "meters"):
            measurement = self.length * 1000
        if (self.unit == "centimeters"):
            measurement = self.length * 10
        elif (self.unit == "millimeters"):
            measurement = self.length

        return round(measurement, 2)
