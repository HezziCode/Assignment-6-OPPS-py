class Product:
    def __init__(self, initial_value):
        self._price = initial_value

    def get_price(self):
        return self._price
    
    def set_price(self, new_value):
        if new_value < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_value

    def del_price(self):
        del self._price

    price = property(get_price, set_price, del_price)


p = Product(f"\nPrice: {100}")     

print(p.price)        

p.price = 150       

print(f"\nUpgraded Price: {p.price}")   

del p.price 

