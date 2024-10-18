# main.py
from os import system
from operation import new_product, purchase_product, sold_product
from read import read_inventory

def heading():
    print("=======================================================")
    print("                   BRJ Furniture")
    print("=======================================================")
    print("Available Stocks, ")
    read_inventory()

def main():
    heading()
    print("=======================================================")
    print("1. Buy")
    print("2. Sell")
    print("3. Exit")
    opt = int(input("Choose Your Option (1/2/3): "))
    print("=======================================================")

    if opt == 1:
        print("1. New Product")
        print("2. Existing Product")
        print("3. Back")
        buy_opt = int(input("Your Choice (1/2/3): "))
        if buy_opt == 1:
            new_product()
        elif buy_opt == 2:
            purchase_product()
        elif buy_opt == 3:
            main()
        else:
            print("Invalid Input, Please enter valid input!")
            main()
    elif opt == 2:
        sold_product()
    elif opt == 3:
        print("Program Terminated!!!")
    else:
        print("Invalid Option, please choose a valid option!")
        main()

if __name__ == "__main__":
    main()
