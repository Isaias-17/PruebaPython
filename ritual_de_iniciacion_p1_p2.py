import time
import csv
#import unittest

class Package():
    quantity = []
    SKUs = []

    def __init__(self, SKU:str, size:int, expired_at:int):
        created = int(round(time.time()))
        #self.SKU = len(self.quantity)
        self.SKU = SKU if (not (SKU in self.SKUs)) else self.setAUniqueSKU(SKU) # we make sure SKU as unique ID
        self.SKUs.append(SKU)
        self.size = size
        #self.expired_at = created + (expired_at * 3600)
        self.expired_at = expired_at
        self.__created_at = created
        self.quantity.append(0)

    def setAUniqueSKU(self, SKU):
        id_cont_aux = len(self.quantity)
        while 1:
            SKU = SKU + str(id_cont_aux)
            if not (SKU in self.SKUs):
                break
            id_cont_aux = id_cont_aux + 1
        return SKU

    def getQuantity(self):
        return len(self.quantity)

    def getTimeToExpire(self):
        return self.expired_at - int(round(time.time()))

    def getTimeSinceCreatedAt(self):
        return int(round(time.time())) - self.__created_at

    @property
    def created_at(self):
        return self.__created_at

class Address():
    def __init__(self, address_line_1, postal_code, locality, city, state, country, address_line_2=None, notes=None):
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.postal_code = postal_code
        self.locality = locality
        self.city = city
        self.state = state
        self.country = country
        self.notes = notes

    def getFullAddress(self):
        return self.address_line_1 + ", " + self.address_line_2 + ", " + self.postal_code + ", " + self.locality + ", " + self.city + ", " + self.state + ", " + self.country + ", " + self.notes

# delivered_at is the same as expired_at in Package class #
class Order(Package):
    def __init__(self, SKU, size, delivered_at, address):
        Package.__init__(self, SKU, size, delivered_at)
        self.delivery_address = address
        self.is_delivered = False

# Function to mark an order as delivered #
def markAsDelivered(order:Order):
    print(order.getTimeToExpire())
    if order.getTimeToExpire() < 0:
        print(f"This package with SKU '{order.SKU}' can not be marked as delivered because the time to deliver has expired.")
    else:
        order.is_delivered = True
        print(f"This package with SKU '{order.SKU}' can be marked as delivered because the time to deliver is ok.")

# Function to read a CSV file #
def readCSV(name_file):
    orders = []
    with open(name_file) as f:
        reader = csv.reader(f)
        i = 0
        for row in reader:
            if i == 0: # Ignoro el encabezado
                i = i + 1
                continue
            print(row[0], "|", row[1], "|", row[2], "|", row[3], "|", row[4], "|", row[5], "|", row[6], "|", row[7], "|", row[8], "|", row[9], "|", row[10])
            orders.append(Order(row[0], int(row[1]), int(row[2]), Address(row[3], row[5], row[6], row[7], row[8], row[9],row[4], row[10])))
    return orders

# Function to get the order with greater difference between created_at and expired_at #
def getOrderWithGreaterDifference(orders:list):
    order = orders[0]
    for o in orders[1:]:
        if (not (o.getTimeToExpire() < 0)) and (o.is_delivered == False):
            if (o.expired_at - o.created_at) > (order.expired_at - order.created_at):
                order = o

    # If any register was right and only our first [0], we check this register if is ok #
    if (not (order.getTimeToExpire() < 0)) and (order.is_delivered == False):
        return order
    return None

if __name__ == '__main__':

    # Example instances about Package class (Part 1) #
    """ p1 = Package("WR524927", 17, 10)
    print(f"Quantity of packages created: {p1.getQuantity()}")
    time.sleep(2)
    p2 = Package("WR524927", 2, 14)
    print(f"Quantity of packages created: {p2.getQuantity()}")
    time.sleep(4)
    p3 = Package("WR524928", 22, 8)
    print(f"Quantity of packages created: {p3.getQuantity()}")

    print(f"P1 created_at {p1.created_at}")
    print(f"P2 created_at {p2.created_at}")
    print(f"P3 created_at {p3.created_at}")
    print(f"ID p1 {p1.SKU}")
    print(f"ID p2 {p2.SKU}")
    print(f"ID p3 {p3.SKU}")
    print(f"Time since the package p1 was created: {p1.getTimeSinceCreatedAt()} seg")
    print(f"Time since the package p2 was created: {p2.getTimeSinceCreatedAt()} seg")
    print(f"Time since the package p3 was created: {p3.getTimeSinceCreatedAt()} seg")
    print(f"Time to the package p1 expire: {p1.getTimeToExpire()} seg")
    print(f"Time to the package p2 expire: {p2.getTimeToExpire()} seg")
    print(f"Time to the package p3 expire: {p3.getTimeToExpire()} seg") """

    # Test Example (Part 2) #
    orders = readCSV("ritual_de_iniciacion.csv")
    for order in orders:
        print(order.SKU, order.delivery_address.getFullAddress())

    markAsDelivered(orders[0])
    markAsDelivered(orders[1])
    markAsDelivered(orders[2])
    markAsDelivered(orders[3])
    time.sleep(40)
    markAsDelivered(orders[4])
    
    order = getOrderWithGreaterDifference(orders)
    if order == None:
        print("All packages were delivered")
    else:
        print(order.SKU)

