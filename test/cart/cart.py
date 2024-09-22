from shop.models import Product
#class braye handle kardna ducntion haye cart site
class Cart:
    
    #If the 'cart' data does not exist creates a new empty dictionary 
    def __init__(self,request ):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart :
            cart = self.session['cart'] = {}
        self.cart = cart 

    #function to decrease the product count
    def decrease(self,product):
        product_id = str(product.id)
        if self.cart[product_id]['quantity'] > 1:
            self.cart[product_id]['quantity'] -= 1
        self.save()
    

    #function to add the product count
    def add(self,product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'price': product.new_price, 'weight': product.weight}
        else:
             if self.cart[product_id]['quantity'] < product.invetntory :
                 self.cart[product_id]['quantity'] += 1
        self.save()

    #function to remove the product 
    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()


    #function to clear the cart
    def clean (self):
        del self.session['cart']
        self.save()

    #function to calculate the price for post by weight
    def post_price(self,product):
        pass 
    
    #function to get total price
    def get_total_price(self):
        price =sum(item['price']*item['quantity'] for item in self.cart.values())
        return price
    

    #in dota ro ham nemidona daqiq baresi shavad
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_final_price(self):
        return self.get_total_price() + self.get_post_price() 
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart_dict = self.cart.copy()
        for product in products:
            cart_dict[str(product.id)]['product'] = product
        for item in cart_dict.values():
            item['total'] = item['price'] * item['quantity']
            yield item

    #fucntion to maek sure it save
    def save(self):
        self.session.modified = True