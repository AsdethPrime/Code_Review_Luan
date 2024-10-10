import sys 
from dataclasses import dataclass
from csv import reader

@dataclass
class Customer():
    id: str | None = None 
    name: str | None = None    
    def get_discount(self, price):
        pass
    
@dataclass
class RetailCustomer(Customer):
    rate_of_discount: float = 0.0    
    def get_discount(self, price: float):
        discount = price * self.rate_of_discount
        return discount    
    def displayCustomer(self):
        print(f"Id = {self.id}| Name = {self.name} | Rate of Discount = {self.rate_of_discount}")

@dataclass
class WholesaleCustomer(Customer):
   rate1: float = 0.0
   rate2: float = 0.0   
   def get_discount(self, price:float):
       discount = (self.rate1 * price ) if (price <= 1000) else (1000 * self.rate1) + ((price - 1000)  * self.rate2)
       # Confirm with teacher if discount is based on price or price * qty 
       return discount   
   def displayCustomer(self):
       print(f"Id = {self.id} | Name = {self.name} | Rate1 = {self.rate1} | Rate2 = {self.rate2}")      

class PartShortException(Exception):
    pass

@dataclass
class Part():
    id: str | None = None
    name: str | None = None
    price: float = 0.0
    onhandqty: int = 0
    def displayPart(self):
        print(f"Part ID = {self.id}| Part Name = {self.name}| Price = {
              self.price}| Quantity on Hand = {self.onhandqty}")  
              
    def replinish(self, amount: int):
        self.onhandqty += amount
        
    def supply(self, amount: int):
        self.onhandqty -= amount
        
@dataclass
class AssembledPart(Part):
    componentpartid1: str | None = None
    componentpartid2: str | None = None
    
    def displayPart(self):
        print(f"Part ID = {self.id}| Part Name = {self.name}| Price = {self.price}| Quantity on Hand = {
              self.onhandqty}| Component part ID1 = {self.componentpartid1}| Component part ID2 = {self.componentpartid2}")
        

class WarehouseManager():
    customers: list[WholesaleCustomer | RetailCustomer] = []
    parts: list[Part] = []
        
    def readParts(self, filename: str):
        parts_fieldnames = ["id", "name", "price", "quantity"]
        assembled_parts_fieldnames = ["id", "name", "price", "part_id1", "part_id2", "quantity"] 
        with open(filename) as parts_file:
            parts_reader = reader(parts_file)
            for row in parts_reader:
                if len(row) == 4:
                    # Parts
                    parts_data = dict(zip(parts_fieldnames, row))
                    id = parts_data["id"].strip()
                    name = parts_data["name"].strip()
                    price = float(parts_data["price"])
                    quantity = int(parts_data["quantity"])                    
                    part = Part(id, name, price, quantity)
                    self.parts.append(part)                   
                    
                
                elif len(row) == 6:
                    #Assembled Parts
                    assembled_parts_data = dict(zip(assembled_parts_fieldnames, row))
                    id = assembled_parts_data["id"].strip()
                    name = assembled_parts_data["name"].strip()
                    price = float(assembled_parts_data["price"])
                    quantity = int(assembled_parts_data["quantity"])
                    componentpartid1 = assembled_parts_data["part_id1"].strip()
                    componentpartid2 = assembled_parts_data["part_id2"].strip()                   
                    part = AssembledPart(id, name, price, quantity, componentpartid1, componentpartid2)
                    self.parts.append(part)                   
                    
                else: 
                    pass
        return self.parts
    
    def readCustomers(self, filename: str): 
        retail_fieldnames = ["id", "name", "discount"]
        wholesale_fieldnames = ["id", "name", "rate1", "rate2"]       
        with open(filename) as customers_file:
            customers_reader = reader(customers_file)
            for row in customers_reader:
                if len(row) == 3:
                    # Retail Customer
                    retail_customer_data = dict(zip(retail_fieldnames, row))
                    id = retail_customer_data["id"]
                    name = retail_customer_data["name"]
                    discount = float(retail_customer_data["discount"])
                    retail_customer = RetailCustomer(id, name, discount)
                    self.customers.append(retail_customer)
                    
                elif len(row) == 4:
                    # Wholesale Customer
                    wholesale_customer_data = dict(zip(wholesale_fieldnames, row))
                    id = wholesale_customer_data["id"]
                    name = wholesale_customer_data["name"]
                    rate1 = float(wholesale_customer_data["rate1"])
                    rate2 = float(wholesale_customer_data["rate2"])
                    
                    wholesale_customer = WholesaleCustomer(id, name, rate1, rate2)
                    self.customers.append(wholesale_customer)
                else: 
                    # Neither retail nor wholesale - ignore
                    pass
        return self.customers
    
    def findPart(self, part_id: str):
        part_requested = None
        for part in self.parts:
            if part.id == part_id:
                part_requested = part
        return part_requested
    
    def findCustomer(self, customer_id: str):
        customer_requested = None
        for customer in self.customers:
            if customer.id == customer_id:
                customer_requested = customer
        return customer_requested
    
    def displayParts(self):
        for part in self.parts:
            part.displayPart()
    
    def displayCustomers(self):
        for customer in self.customers:
            customer.displayCustomer()

class WarehouseManagerUI:

    warehousemanager = WarehouseManager()

    def run_warehouse_manager(self):
        customer_file_name = "customers.txt"
        parts_file_name = "parts.txt"
        if (self.warehousemanager.readCustomers(customer_file_name)==None):
            sys.stdout.write("Could not load file: "+customer_file_name)
        if (self.warehousemanager.readParts(parts_file_name)==None):
            sys.stdout.write("Could not load file: "+parts_file_name)

        choice = self.get_menu_choice()
        while (choice != "q"):
            sys.stdout.write("\n")
            if (choice=="r"):
                self.replenish()
            elif (choice=="s"):
                self.supply()
            elif (choice=="a"):
                self.assemble()
            elif (choice=="d"):
                self.warehousemanager.displayParts()
            elif (choice=="c"):
                self.warehousemanager.displayCustomers()
            choice = self.get_menu_choice()



    def get_menu_choice(self):
        menu="\n===================\n"
        menu+="Warehouse Manager   \n"
        menu+="[R]eplenish a part  \n"
        menu+="[S]upply a part     \n"
        menu+="[A]ssemble a part   \n"
        menu+="[D]isplay all parts \n"
        menu+="Display all [C]ustomers \n"
        menu+="[Q]uit              \n"

        sys.stdout.write(menu)
        menu=menu.lower()
        choice=self.get_str("Enter choice: ").lower()
        while not "["+choice+"]" in menu:
            choice = self.get_str(choice+" was an invalid choice! Re-enter: ").lower()
        return choice

    def get_str(self, prompt):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        value = sys.stdin.readline().strip()
        while (len(value)==0):
            sys.stdout.write("Input cannot be blank. Re-enter:")
            sys.stdout.flush()
            value = sys.stdin.readline().strip()

        return value

    def get_int(self, prompt):
        value=None
        while (value==None):
            try:
                value=int(self.get_str(prompt))
            except:
                prompt="Please enter an integer value"
        return value
    
    def replenish(self):
        part_id = self.get_str("Enter part id: ")
        quantity = self.get_int("Enter quantity: ")        
        part_to_update = self.warehousemanager.findPart(part_id)        
        if part_to_update:
            part_to_update.replinish(quantity)
            print(part_to_update)
        else:
            print(f"Part ID {part_id} was not found")      
        
    
    def supply(self):
        part_id = self.get_str("Please enter part id: ")
        customer_id = self.get_str("Please enter customer id: ")
        quantity = self.get_int("Please enter quantity: ")        
        part = self.warehousemanager.findPart(part_id)
        if not part:
            print(f"Part ID {part_id} not found")
            return None        
        customer = self.warehousemanager.findCustomer(customer_id)
        if not customer:
            print(f"Cutomer ID {customer_id} not found")
            return None        
        if not part.onhandqty >= quantity:
            raise PartShortException(f"{part_id}, {part.name}")        
        price = part.price * quantity
        discount = customer.get_discount(price)
        price_to_pay = price - discount        
        print(f"Total cost = {price} , discount = {discount} , price to pay = {price_to_pay}")
        part.supply(quantity)
        print(part)
        
    
    def assemble(self):
        assembled_part_id = self.get_str("Please enter assemble part id: ")
        assembled_part = self.warehousemanager.findPart(assembled_part_id)
        if not assembled_part:
            print(f"Assemble part ID: {assembled_part_id} not found")
            return None
        component_part_id1 = assembled_part.componentpartid1
        component_part_id2 = assembled_part.componentpartid2
        
        component1 = self.warehousemanager.findPart(component_part_id1)
        component2 = self.warehousemanager.findPart(component_part_id2)
        
        if not component1.onhandqty > 0:
            raise PartShortException(f"{component1.id} and {component1.name}")
        if not component2.onhandqty > 0:
            raise PartShortException(f"{component2.id} and {component2.name}")
                
        component1.supply(1)
        component2.supply(1)
        assembled_part.replinish(1)


##Testing your application
warehousemanagerUI = WarehouseManagerUI()
warehousemanagerUI.run_warehouse_manager()
