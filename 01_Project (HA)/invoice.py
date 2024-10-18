from datetime import date
from main import main

def invoice(is_purchased_or_sold,product, quantity, price_per_unit, total_price):
    print("\n")
    print("*********** INVOICE ***********")
    print(f"Date : {date.today()}")
    if is_purchased_or_sold:
        transaction_type = "Purchased"
    else:
        transaction_type="Sold"
    print(f"Transaction Type: {transaction_type} ")
    print("*******************************")
    print(f"Product: {product}")
    print(f"Quantity: {quantity}")
    print(f"Price per Unit: ${price_per_unit}")
    print(f"Total Price: ${total_price}")
    print("*******************************")
    print("Hope you have a great experience:)")
    print("*******************************\n")
    print("\n")
    opt = input("Do you wanna buy again: (Y/N) ")
    if opt == 'Y' or opt == 'y':
        main()
    else:
        exit()