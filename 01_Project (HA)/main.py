
#BRJ Furniture
from newProduct import *
from purchased import *
from sold import *

#functions
def heading():    
    #heading
    print("=======================================================")
    print("                   BRJ Furniture")
    print("=======================================================")

    #prints the avaliable stocks from the file
    print("Available Stocks, ")
    with open("furniture.txt") as f:
        print(f.read())
        
         
# #function for buying new product    
# def new_product():
#     id = int(input("Enter ID: "))
#     co_name=input("Enter Company Name: ")
#     product= input("Enter Product: ")
#     quantity=int(input("Enter the quantity: "))
#     price_per_unit=float(input("Enter price (per unit):"))
#     total_price = quantity*price_per_unit
#     text = f"{id}, {co_name}, {product}, {quantity}, ${total_price}"
#     is_purchased = True
#     with open("furniture.txt",'a') as f:
#         f.write("\n")
#         f.write(text)
#     invoice(is_purchased,product, quantity, price_per_unit, total_price)
    
  
# #function for buying existing product
# def purchase_product():
#     purchase_item =input("Enter the product name you bought: ")
#     qty = int(input("Enter the quantity you bought:"))
#     is_purchase= True
#     update_product(purchase_item, qty,is_purchase)   
    
# #function for selling
# def sold_product():
#     selling_item = input("Enter the product you want to sell: ")
#     qty = int(input("Enter the quantity you want to sell: "))
#     is_purchased = False
#     update_product(selling_item,qty, is_purchased)
    
# #update the value after purchase and sell       
# def update_product(search,qty, is_purchased):
#     print("=======================================================")
#     with open("furniture.txt", 'r') as f:
#         # read every lines as list
#         contents = f.readlines()
    
#     # defining an empty array for storing the search result  
#     result =[]
#     for content in contents:
#         if search in content:
#                result.append(content)
               
#     if(len(result)>1):
#         print("More than one result found,Please Select")
#         print("=======================================================")
#         # printing the search result
#         for items in result:
#             print(items)
             
#         result_opt = int(input("Enter your Choice: "))
#         selected_item = result[result_opt-1]
        
#     elif(len(result)==1):
#         selected_item = result[0]
        
#     else:
#         system("clear")
#         print(f"No items found!!! for `{search}`")
#         main()
#         return
    
#     # converting the list in array form
#     arr = selected_item.strip().split(", ")
#     curr_qty = int(arr[3])
    
#     # updating the valuse
#     if is_purchased:
#         new_qty = qty + curr_qty
#         org_price = float(arr[4].strip("$"))
#         price_per_unit = org_price/curr_qty
#         new_price = org_price + (qty * price_per_unit)
#     else:
#         new_qty = curr_qty - qty
#         org_price = float(arr[4].strip("$"))
#         price_per_unit = org_price/curr_qty
#         new_price = org_price - (qty * price_per_unit)
        
#     update_text = f"{arr[0]}, {arr[1]}, {arr[2]}, {new_qty}, ${new_price}\n"     

#     # writing the updated text
#     with open("furniture.txt", 'w') as f:
#         for item in contents:
#             if item.strip() == selected_item.strip():
#                 f.write(update_text)
#             else:
#                 f.write(item)
#     print(f"Product Updated Successfully, '{arr[2]}' with new quantity: {new_qty} and new price: {new_price}")
#     #generating invoice
#     invoice(is_purchased,arr[2],qty,price_per_unit,qty*price_per_unit)
    
# # Invoice Generation
# def invoice(is_purchased_or_sold,product, quantity, price_per_unit, total_price):
#     print("\n")
#     print("*********** INVOICE ***********")
#     print(f"Date : {date.today()}")
#     if is_purchased_or_sold:
#         transaction_type = "Purchased"
#     else:
#         transaction_type="Sold"
#     print(f"Transaction Type: {transaction_type} ")
#     print("*******************************")
#     print(f"Product: {product}")
#     print(f"Quantity: {quantity}")
#     print(f"Price per Unit: ${price_per_unit}")
#     print(f"Total Price: ${total_price}")
#     print("*******************************")
#     print("Hope you have a great experience:)")
#     print("*******************************\n")
        

# Main function or landing function       
def main():
    heading()
    print("1. Buy")
    print("2. Sell")
    print("3. Exit")
    opt = int(input("Choose Your Option (1/2/3): "))
    print("=======================================================")
    #switch-case
    def switch(opt):
        match(opt):
            case 1:
                print("1. New Product")
                print("2. Existing Product")
                print("3. Back")
                buy_opt =int(input("Your Choice (1/2/3):"))
                if(buy_opt==1):
                    new_product()
                    print("New Product Added Successfully, :)")
                elif(buy_opt==2):
                    purchase_product() 
                elif(buy_opt==3):
                    system('clear')
                    main() 
                else:
                    system('clear')
                    print("Invalid Input, Please enter valid input!!!!!!")
                    main()
                    
            case 2:
                sold_product()
                
            case 3:
                system("clear")
                print("Program Terminated!!!")
                
            #Default or values outside the option
            case _:
                system("clear")
                print("Invalid Option, please choose a valid option!")
                main()
    switch(opt)

#program flow
main()

