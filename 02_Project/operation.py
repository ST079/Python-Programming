# operations.py
from datetime import date
from os import system
from write import write_inventory
from read import read_inventory

def new_product():
    from main import main
    id = int(input("Enter ID: "))
    co_name = input("Enter Company Name: ")
    product = input("Enter Product: ")
    quantity = int(input("Enter the quantity: "))
    price_per_unit = float(input("Enter price (per unit): "))
    total_price = quantity * price_per_unit
    text = f"{id}, {co_name}, {product}, {quantity}, ${total_price}"
    with open("furniture.txt", 'a') as f:
        f.write("\n" + text)
    invoice(True, product, quantity, price_per_unit, total_price)

def purchase_product():
    purchase_item = input("Enter the product name you bought: ")
    qty = int(input("Enter the quantity you bought: "))
    update_product(purchase_item, qty, True)

def sold_product():
    selling_item = input("Enter the product you want to sell: ")
    qty = int(input("Enter the quantity you want to sell: "))
    update_product(selling_item, qty, False)

def update_product(search, qty, is_purchased):
    contents = read_inventory()
    result = [content for content in contents if search in content]

    if len(result) > 1:
        print("More than one result found, Please Select")
        for index, items in enumerate(result):
            print(f"{index + 1}. {items.strip()}")
        result_opt = int(input("Enter your Choice: ")) - 1
        selected_item = result[result_opt]
    elif len(result) == 1:
        selected_item = result[0]
    else:
        print(f"No items found!!! for `{search}`")
        return

    arr = selected_item.strip().split(", ")
    curr_qty = int(arr[3])

    if is_purchased:
        new_qty = qty + curr_qty
        org_price = float(arr[4].strip("$"))
        price_per_unit = org_price / curr_qty
        new_price = org_price + (qty * price_per_unit)
    else:
        new_qty = curr_qty - qty
        org_price = float(arr[4].strip("$"))
        price_per_unit = org_price / curr_qty
        new_price = org_price - (qty * price_per_unit)

    update_text = f"{arr[0]}, {arr[1]}, {arr[2]}, {new_qty}, ${new_price}\n"
    write_inventory(contents, selected_item, update_text)
    invoice(is_purchased, arr[2], qty, price_per_unit, qty * price_per_unit)

def invoice(is_purchased_or_sold, product, quantity, price_per_unit, total_price):
    from main import main
    print("\n*********** INVOICE ***********")
    print(f"Date : {date.today()}")
    transaction_type = "Purchased" if is_purchased_or_sold else "Sold"
    print(f"Transaction Type: {transaction_type}")
    print(f"Product: {product}")
    print(f"Quantity: {quantity}")
    print(f"Price per Unit: ${price_per_unit}")
    print(f"Total Price: ${total_price}")
    print("*******************************")
    opt = input("Do you want to buy again : (y/n): ")
    if ( opt == 'y' or opt == 'Y'):
        system('clear')
        main()
    else :
        exit()
