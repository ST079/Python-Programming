from main import main
from os import system
from invoice import *

def update_product(search,qty, is_purchased):
    print("=======================================================")
    with open("furniture.txt", 'r') as f:
        # read every lines as list
        contents = f.readlines()
    
    # defining an empty array for storing the search result  
    result =[]
    for content in contents:
        if search in content:
               result.append(content)
               
    if(len(result)>1):
        print("More than one result found,Please Select")
        print("=======================================================")
        # printing the search result
        for items in result:
            print(items)
             
        result_opt = int(input("Enter your Choice: "))
        selected_item = result[result_opt-1]
        
    elif(len(result)==1):
        selected_item = result[0]
        
    else:
        system("clear")
        print(f"No items found!!! for `{search}`")
        main()
        return
    
    # converting the list in array form
    arr = selected_item.strip().split(", ")
    curr_qty = int(arr[3])
    
    # updating the valuse
    if is_purchased:
        new_qty = qty + curr_qty
        org_price = float(arr[4].strip("$"))
        price_per_unit = org_price/curr_qty
        new_price = org_price + (qty * price_per_unit)
    else:
        new_qty = curr_qty - qty
        org_price = float(arr[4].strip("$"))
        price_per_unit = org_price/curr_qty
        new_price = org_price - (qty * price_per_unit)
        
    update_text = f"{arr[0]}, {arr[1]}, {arr[2]}, {new_qty}, ${new_price}\n"     

    # writing the updated text
    with open("furniture.txt", 'w') as f:
        for item in contents:
            if item.strip() == selected_item.strip():
                f.write(update_text)
            else:
                f.write(item)
    print(f"Product Updated Successfully, '{arr[2]}' with new quantity: {new_qty} and new price: {new_price}")
    #generating invoice
    invoice(is_purchased,arr[2],qty,price_per_unit,qty*price_per_unit)