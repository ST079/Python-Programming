from updateProduct import *

#function for buying existing product
def purchase_product():
    purchase_item =input("Enter the product name you bought: ")
    qty = int(input("Enter the quantity you bought:"))
    is_purchase= True
    update_product(purchase_item, qty,is_purchase)  