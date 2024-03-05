class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        return f"ID: {self.id}, Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                return f"Product with ID {product_id} removed."
                return
        return f"Product with ID {product_id} not found."

    def display_inventory(self):
        print("Inventory:")
        for product in self.products:
            product.display()

print("1.Display \n2.Add_Product \n3.Remove_Product \n4.Display_Invertory\n")
while True:
    option = input("Enter Choice: ")

    inventory = Inventory()
    if option == '1':
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        price = input("Enter Price: ")
        quantity = input("Enter Quantity: ")
        product1 = Product(id, name, price, quantity)
        print(product1.display())
    elif option == '2':
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        price = input("Enter Price: ")
        quantity = input("Enter Quantity: ")
        product1 = Product(id, name, price, quantity)
        inventory.add_product(product1)
    elif option == '3':
        id = input("Enter ID: ")
        print(inventory.remove_product(id))
    elif option == '4':
        print(inventory.display_inventory())
    







