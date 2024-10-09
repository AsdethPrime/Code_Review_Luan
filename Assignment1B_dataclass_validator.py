from dataclasses import dataclass


@dataclass
class Part():
    id: str | None = None
    name: str | None = None
    price: float = 0.0
    onhandqty: int = 0

    def displayPart(self):
        """Prints Parts values as a formatted string"""
        message = f"Part ID = {self.id}| Part Name = {self.name}| "
        message += f"Price = {self.price}| Quantity on Hand = {self.onhandqty}"
        print(message)


@dataclass
class AssembledPart(Part):
    componentpartid1: str | None = None
    componentpartid2: str | None = None

    def displayPart(self):
        """Print Assembled Part values as a formatted string"""
        message = f"Part ID = {self.id}| Part Name = {self.name}| "
        message += f"Price = {self.price} Quantity on Hand = {self.onhandqty}| "
        message += f"Component part ID1 = {
            self.componentpartid1} |Component part ID2 = {self.componentpartid2}"
        print(message)

class DataValidator():
    """Check if each parameters are valid, in not print an error message and exit"""

    def validatePart(self, id: str, name: str, price: float, onhandqty: int):
        self.validateID(id)
        self.validateName(name)
        self.validatePrice(price)
        self.validateQtyOnHand(onhandqty)

    def validateAssembledPart(self, id: str, name: str, price: float, onhandqty: int, componentID1: str, componentID2: str):
        self.validateID(id)
        self.validateName(name)
        self.validatePrice(price)
        self.validateQtyOnHand(onhandqty)
        self.validateID(componentID1)
        self.validateID(componentID2)

    @staticmethod
    def printError(message):
        """Prints error message in red and bold"""
        redBold = "\033[91;1m"
        reset = "\033[0m"
        print(f"{redBold}[!ERROR] {message} [!ERROR]{reset}")

    def validateID(self, id: str):
        if not id.strip():
            self.printError("Id cannot be an empty string, exiting!")
            exit(1)

    def validateName(self, name: str):
        if not name.strip():
            self.printError("Name cannot be an empty string, exiting")
            exit(1)

    def validatePrice(self, price: float):
        try:
            price = float(price)
        except ValueError:
            self.printError("Price needs to be a floating point number")
            exit(1)
        
        if price < 0.0:
            self.printError("Price can't be negative")
            exit(1)

    def validateQtyOnHand(self, onhandqty: int):
        try:
            onhandqty = int(onhandqty)
        except ValueError:
            self.printError("Quantity on Hand needs to be an integer")
            exit(1)

        if onhandqty < 0:
            self.printError("Quantity on hand can't be negative")
            exit(1)


class DataFormatter():
    @staticmethod
    def formatPartData(id: str, name: str, price: float, onhandqty: int):
        formattedData =  {
        "id": id.strip(),
        "name": name.strip(),
        "price": float(price),
        "onhandqty": int(onhandqty),
        }
        return formattedData
    
    @staticmethod
    def formatAssembledPartData(id: str, name: str, price: float, onhandqty: int, componentID1: str, componentID2: str):
        formattedData = {
            "id": id.strip(),
            "name": name.strip(),
            "price": float(price),
            "onhandqty": int(onhandqty),
            "componentpartid1": componentID1.strip(),
            "componentpartid2": componentID2.strip()
        }
        return formattedData


class ControllerClass():
    parts: list[Part] = []
    validator: DataValidator = DataValidator()
    fomatter: DataFormatter = DataFormatter()

    def addPart(self, id: str, name: str, price: float, onhandqty: int):
        self.validator.validatePart(id, name, price, onhandqty)
        formattedPartData = self.fomatter.formatPartData(id, name, price, onhandqty)
        part = Part(**formattedPartData)
        self.parts.append(part)
        # message to say this has been added
        part.displayPart()

    def addAssembledPart(self, id: str, name: str, price: float, qtyonhand: int, componentID1: str, componentID2: str):
        self.validator.validateAssembledPart(id, name, price, qtyonhand, componentID1, componentID2)
        formattedAssembledPart = self.fomatter.formatAssembledPartData(id, name, price, qtyonhand, componentID1, componentID2)
        assembledPart = AssembledPart(**formattedAssembledPart)
        self.parts.append(assembledPart)
        # message to say this has been added
        assembledPart.displayPart()

    def displayParts(self):
        for n in range(0, len(self.parts)):
            self.parts[n].displayPart()




controller = ControllerClass()
controller.addPart("P1", "Large Octopus", 21.00, 3)
controller.addPart("P2", "Small Barnacle", 1.00, 3)
controller.addAssembledPart("P3", "Barnacle on Octopus", 24.00, 0, "P1", "P2")
controller.displayParts()
