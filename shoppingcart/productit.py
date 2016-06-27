class productit(object):
    def __init__(self, _product, _quantity, _price, _category): 
        self.product = _product                                   
        self.quantity = int(_quantity)                            
        self.price = float(_price)                               
        self.category = _category                                 
        self.totalPrice = int(_quantity) * float(_price)        
        

		
if __name__ == "__main__":
    Product("iphone",5,5,"電子")
