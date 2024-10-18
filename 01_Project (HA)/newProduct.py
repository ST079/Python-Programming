from invoice import *
#function for buying new product    
def new_product():
    id = int(input("Enter ID: "))
    co_name=input("Enter Company Name: ")
    product= input("Enter Product: ")
    quantity=int(input("Enter the quantity: "))
    price_per_unit=float(input("Enter price (per unit):"))
    total_price = quantity*price_per_unit
    text = f"{id}, {co_name}, {product}, {quantity}, ${total_price}"
    is_purchased = True
    with open("furniture.txt",'a') as f:
        f.write("\n")
        f.write(text)
    invoice(is_purchased,product, quantity, price_per_unit, total_price)