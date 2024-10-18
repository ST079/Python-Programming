from updateProduct import *
#function for selling
def sold_product():
    selling_item = input("Enter the product you want to sell: ")
    qty = int(input("Enter the quantity you want to sell: "))
    is_purchased = False
    update_product(selling_item,qty, is_purchased)