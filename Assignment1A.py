import sys

def main():
    sectionSeparator("Initialise Product")
    numberOfProducts = integerInput("How many products do you want to enter: ")
    productList = initProducts(numberOfProducts)

    sectionSeparator("Initialize Customers")
    numberOfCustomers = integerInput("How many customers do you want to enter: ")
    customerList = initCustomers(numberOfCustomers)   
  
    sectionSeparator("Take Order")
    nameOfCustomer = stringInput("Enter the name of customer: ")
    nameOfPart = inputValidPart(productList)
    quantityPurchased = integerInput("Enter the quantity purchased: ")

    sectionSeparator("Print Total")
    productPrice = productList.get(nameOfPart, 0)
    customerDiscount = customerList.get(nameOfCustomer, 0)
    totalPrice = totalPriceCalculator(productPrice, customerDiscount, quantityPurchased)
    message = f"Hello {nameOfCustomer} "
    message += f"You have purchased {quantityPurchased} of {nameOfPart} - unit price {productPrice}."
    message += f"Your total price is {totalPrice:.2f}"
    print(message)
    return None



def initProducts(numberofproducts):
    ''' Creates and returns a dictionary of products and prices'''
    sys.stdout.write("Initialising product data\n")
    products = {}
    numberofproducts += 1
    for n in range(1, numberofproducts):
        sys.stdout.write("Enter the name of part "+str(n)+"\n")
        productname = sys.stdin.readline().strip()
        sys.stdout.write("Enter the unit price of part" + str(n)+"\n")
        productprice = float(sys.stdin.readline())
        products[productname] = productprice
    print(products)
    return products


def initCustomers(numberoOfCustomers):
    '''Creates and returns a dictionary of customers and discounts'''
    print("Initialising customer data")
    customers = {}
    numberOfCustomers += 1
    for n in range(1, numberOfCustomers):
        customerName = stringInput(f"Enter the name of customer {n} \n")
        customerDiscount = floatInput("Enter associated discount for the customer (.10 is 10%): ")
        customers[customerName] = customerDiscount
    print(customers)
    return customers


totalPriceCalculator = lambda productPrice, customerDiscount, quantityPurchased: (1 - customerDiscount) * productPrice * quantityPurchased


def integerInput(messageString):
    """Forces user to input a positive integer, if incorrect data is provided the user is asked to try again"""
    while True:
        try:
            sys.stdout.write(messageString)
            sys.stdout.flush()
            value = int(sys.stdin.readline().strip())
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            printError("Please enter a positive integer")

            
def stringInput(message):
    """Forces user to input a non-empty string"""
    while True:
        try:
            sys.stdout.write(message)
            sys.stdout.flush()
            value = sys.stdin.readline().strip()
            if value:
                return value                
            else:
                raise ValueError
        except ValueError:
            printError("Input cannot be blank. Please try again")
 

def floatInput(message):
    """Forces user to input a float between 0 - 1, if incorrect data is provided the user is asked to try again"""
    while True:
        try:
            sys.stdout.write(message)
            sys.stdout.flush()
            value = float(sys.stdin.readline().strip())
            if value >= 1 or value < 0:
                raise ValueError
            return value
        except ValueError:
            printError("Enter a float between 0.00 to 1.00")



def inputValidPart(productlist):
    """Forces user to input a valid part from productlist"""
    while True:
        nameOfPart = stringInput("Enter the name of a part: ")
        if productlist.get(nameOfPart):
            return nameOfPart
        else:
            printError(f"We do not have {nameOfPart}; please try again")

def printError(message):
    """Prints error message in red and bold"""    
    redBold = "\033[91;1m"
    reset = "\033[0m"
    print(f"{redBold}[!ERROR] {message} [!ERROR]{reset}")
    
def sectionSeparator(section_name):
    """Displays a custom seperator to seperate different sections """
    separator = '*' * 20
    print(f"\n{separator} {section_name} {separator}\n")


if __name__ == "__main__":
    main()
