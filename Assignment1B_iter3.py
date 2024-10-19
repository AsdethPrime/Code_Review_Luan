class Part():
    def __init__(self, id, name, price, onhandqty):
        self.id = id
        self.name = name
        self.price = price
        self.onhandqty = onhandqty

    def displayPart(self):
        print(f"""Part ID = {self.id} Part Name = {self.name} Price = {
              self.price} Quantity on Hand = {self.onhandqty}""")


class AssembledPart(Part):
    def __init__(self, id, name, price, onhandqty, componentpartid1, componentpartid2):
        super().__init__(id, name, price, onhandqty)
        self.componentpartid1 = componentpartid1
        self.componentpartid2 = componentpartid2

    def displayPart(self):
        print(f"""Part ID = {self.id} Part Name = {self.name} Price = {self.price} Quantity on Hand = {
              self.onhandqty} Component part ID1 = {self.componentpartid1} Component part ID2 = {self.componentpartid2}""")
        
class ControllerClass():
    def __init__(self):
        self.parts = []
        
    def addPart(self, id, name, price, qtyonhand):
        part = Part(id, name, price, qtyonhand)
        self.parts.append(part)
        # message to say this has been added
        part.displayPart()

    def addAssembledPart(self, id, name, price, qtyonhand, componentID1, componentID2):
        assembled_part = AssembledPart(id, name, price, qtyonhand, componentID1, componentID2)
        self.parts.append(assembled_part)
        # message to say this has been added
        assembled_part.displayPart()

    def displayParts(self):
        for n in range(0, len(self.parts)):
            self.parts[n].displayPart()


controller = ControllerClass()
controller.addPart("P1", "Large Octopus", 21.00, 3)
controller.addPart("P2", "Small Barnacle", 1.00, 3)
controller.addAssembledPart("P3", "Barnacle on Octopus", 24.00, 0, "P1", "P2")
controller.displayParts()
