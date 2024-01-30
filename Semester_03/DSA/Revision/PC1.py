class OnlineCart:
    def __init__ (self):
        self.cart = []
        self.size = 0
        
    def insertcartprice(self,price):
        self.cart.append(price)
        self.size +=1
    
    def total(self):
        i = 0
        totalprice = 0
        while i <= len(self.cart) -1:
            totalprice = totalprice + self.cart[i]
            i+=1  
        return totalprice

    def display (self):
        i = 0
        while i <= len(self.cart) -1:
            print (i,self.cart[i])
            i+=1

Cart = OnlineCart()
Cart.insertcartprice(5)
Cart.insertcartprice(5)
Cart.insertcartprice(4.99)
Cart.insertcartprice(1.99)
Cart.insertcartprice(11)
Cart.insertcartprice(10)
Cart.display()
print('\n', "Total Price: $%.2f " %Cart.total())