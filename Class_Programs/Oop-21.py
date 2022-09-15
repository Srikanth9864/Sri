class ShoppingCart:
    # class Variable
    prices = { "iPhone": 800, "iMac": 2500, "iWatch": 3000, "iPad": 3500 }
    products = { "iPhone": 5, "iMac": 3, "iWatch": 2, "iPad": 4 }

    def __init__(self):
        self.cart = [ ]
    
    def add_item(self, name, quantity):
        if name not in ShoppingCart.products:
            raise Exception("Product not available")
        elif quantity > ShoppingCart.products[name]:
            raise Exception("Product out of stock")
        else:
            self.cart.append({ "name": name, "quantity": quantity, "price":  ShoppingCart.prices[name]})
            
            ShoppingCart.products[name] -= quantity

    def remove_item(self, name):
        for item in self.cart:
            if name == item['name']:
                if item['quantity'] > 1:
                    item['quantity'] = item['quantity'] - 1
                else:
                    self.cart.remove(item)
    
    def total_cost(self):
        total = 0.00
        for item in self.cart:
            total += item['quantity'] * item['price']
        return total

c1 = ShoppingCart()
c2 = ShoppingCart()
