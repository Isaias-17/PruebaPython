class Locations():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vales = []
        self.setValues(x * y * z)

    def setValues(self, size):
        self.values = []
        for i in range(size):
            self.values.append("")

    def addValue(self, value, x, y, z):
        position = ((x - 1) * 1) + ((y - 1) * self.x) + ((z - 1) * (self.x * self.y))
        self.values[position] = value

    def getValue(self, x, y, z):
        position = ((x - 1) * 1) + ((y - 1) * self.x) + ((z - 1) * (self.x * self.y))
        return self.values[position]

    def showValues(self):
        print("Z, Y, X")
        for z in range(self.z):
            for y in range(self.y):
                for x in range(self.x):
                    print(f"{z + 1}, {y + 1}, {x + 1} => {self.getValue(x + 1, y + 1, z + 1)}")

# Test Example in a Locations with x=3, y=4 and z=7 #
locations_a = Locations(3, 4, 7)
print(len(locations_a.values))

locations_a.addValue("Hola Mundo", 1, 3, 7)
print(locations_a.values[78])
print(locations_a.getValue(1, 3, 7))

locations_a.addValue("Hola Cargamos", 2, 2, 2)
print(locations_a.values[16])
print(locations_a.getValue(2, 2, 2))

locations_a.showValues()

# Test Example in a Locations with x=4, y=4 and z=4 #
locations_b = Locations(4, 4, 4)
print()
print(len(locations_b.values))

locations_b.addValue("Hola Logistics", 1, 4, 2)
print(locations_b.values[28])
print(locations_b.getValue(1, 4, 2))

locations_b.addValue("Hola Tech", 1, 1, 1)
print(locations_b.values[0])
print(locations_b.getValue(1, 1, 1))

locations_b.showValues()