# this file contains the frontend activity such as design,structure etc..
import pickle
from tabulate import tabulate
import datetime
import colorama
from Database.path_helper import get_path

storage = dict()

def display_design():
    f1 = open(get_path("Database/database.dat"),"rb")
    f2 = open(get_path("Database/Product_Number.dat"),"rb")
    data = pickle.load(f1)
    Product_list = pickle.load(f2)
    Product_Name = []
    Product_Rate = []
    for x in data.keys():
        Product_Name.append(x)
    for y in data.values():
        Product_Rate.append(y)
    print(colorama.Style.BRIGHT + colorama.Fore.RED)
    display_Table = {
        "Product_Number" : Product_list,
        "Product Name ": Product_Name,
        "Retail Price ": Product_Rate
                    }
    print(tabulate(display_Table, headers="keys" ,tablefmt = "fancy_grid"))
    print(colorama.Style.RESET_ALL)
    f1.close()
    f2.close()


def display_design_cart():
    f1 = open(get_path("Database/My_Shopping_Cart.dat"),"rb")
    f2 = open(get_path("Database/total.dat"),"rb")
    f3 = open(get_path("Database/net_quantity.dat"),"rb")
    f4 = open(get_path("Database/retail.dat"),"rb")
    f5 = open(get_path("Database/Coupon Code.dat"),"rb")
    f6 = open(get_path("Database/bill.dat"),"wb")
    f7 = open(get_path("Database/code_cheats.dat"),"rb")
    f8 = open(get_path("Data_Storage/storage.dat"),"wb")
    data = pickle.load(f1)        # My cart
    data_2 = pickle.load(f2)      # total
    data_3 = pickle.load(f3)      # net quantity
    data_4 = pickle.load(f4)      # retail
    data_5 = pickle.load(f5)
    retail = data_4
    code = pickle.load(f7)
    items = []
    for x in data.keys():
        items.append(x)
    total = data_2
    while True :
        OFFER = input("Enter Discount Code :")
        if OFFER in code.keys():
            x = code.get(OFFER)
            break
        else :
            print("Code is not Valid!:")
    user_discount = x
    total_bill = sum(total) * user_discount / 100
    net_quantity = data_3
    x = datetime.datetime.now()
    y = x.strftime("%D")
    s = x.strftime("%T")
    z = [f"Date:{y}",f"Savings:RS {round(sum(total)-total_bill,2)}/-",f"Offer:{OFFER}", f"\nTime:{s}\nThank You Visit Again!\n\nTotal Amount :{total_bill}"]
    cart_table = {
        "Product Name": items,
        "Net Quantities" : net_quantity,
        "Retail Price" : retail,
        "Total " : total,
        f"CUSTOMER ID:{data_5} :" : z
    }
    print(colorama.Fore.RED + colorama.Style.BRIGHT)
    print(tabulate(cart_table, headers="keys", tablefmt="psql"))
    print(colorama.Style.RESET_ALL)
    info = [ f"Date:{y}{s}",f"Savings:RS {round(sum(total)-total_bill,2)}/-",f"Offer: {OFFER}", f"Total Amount :{total_bill}"]
    storage[data_5] = info
    storage.update()
    pickle.dump(storage,f8)
    pickle.dump(total_bill,f6)
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()

def display_chocolate():
    f1 = open(get_path("Database/chocolate_data.dat"),"rb")
    f2 = open(get_path("Database/chocolates_count.dat"),"rb")
    count = pickle.load(f2)
    data = pickle.load(f1)
    items = []
    rate = []
    print(colorama.Style.BRIGHT + colorama.Fore.GREEN)
    for r in data.values():
        rate.append(r)
    for x in data.keys():
        items.append(x)
    chocolate_table = {
        "Product Number" : count,
        "Product Name" : items,
        "Retail Price" : rate
    }
    print(tabulate(chocolate_table, headers="keys", tablefmt="fancy_grid"))
    print(colorama.Style.RESET_ALL)
    f1.close()
    f2.close()

def display_stationary():
    f1 = open(get_path("Database/stationary_data.dat"),"rb")
    f2 = open(get_path("Database/Product_Number.dat"),"rb")
    f3 = open(get_path("Database/chocolates_count.dat"),"rb")
    data = pickle.load(f1)
    total_count = pickle.load(f2)
    choco_count = pickle.load(f3)
    updating_count= choco_count[-1] - 1
    items = []
    rate = []
    print(colorama.Style.BRIGHT + colorama.Fore.BLUE)
    for x in data.keys():
        items.append(x)
    updated_items = items[::-1]
    for y in data.values():
        rate.append(y)
    Product_Number = total_count[:updating_count:-1]
    updated_rate = rate[::-1]
    stationary_table = {
        "Product Number" : Product_Number,
        "Product Name" : updated_items,
        "Retail Price" : updated_rate
    }
    print(tabulate(stationary_table, headers="keys", tablefmt="fancy_grid"))
    print(colorama.Style.RESET_ALL)
    f1.close()
    f2.close()
    f3.close()

def display_function():
    print(colorama.Style.NORMAL + colorama.Fore.LIGHTGREEN_EX)
    Function_Keys = ['S','R','F','B','H','Q']
    Function_Name = ["Sorting","Budget Range","Find","Buy","Help","Quit"]
    function_table = {
        "Function" : Function_Name,
        "Keys" : Function_Keys
    }
    print(tabulate(function_table, headers="keys", tablefmt="double_grid"))
    print(colorama.Style.RESET_ALL)

def sort_design():
    print(colorama.Fore.RED)
    sorting_items = ["Chocolates","Stationary"]
    sorting_keys = [" C "," S "]
    sort_table = {
        " ITEMS ": sorting_items,
        " Sorting-Keys " : sorting_keys
    }
    print(tabulate(sort_table, headers="keys" , tablefmt="fancy_grid"))
    print(colorama.Style.RESET_ALL)

def budget_design():
    f1 = open(get_path("Database/Budget_Range.dat"),"rb")
    data = pickle.load(f1)
    items = []
    costs = []
    for x in data.keys():
        items.append(x)
    for y in data.values():
        costs.append(y)
    table = {
        "Product Name" : items,
        "Costs in RS/-": costs
    }
    print(colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX)
    print(tabulate(table, headers="keys" , tablefmt="double_grid"))
    print(colorama.Style.RESET_ALL)
    f1.close()

def Bill():
    f1 = open(get_path("Database/Mart_Bill.dat"),"rb")
    f2 = open(get_path("Database/Mart_Value.dat"),"rb")
    f3 = open(get_path("Database/Mart_Total.dat"),"rb")
    f4 = open(get_path("Database/net_quantity.dat"),"rb")
    f5 = open(get_path("Database/total.dat"),"rb")
    f6 = open(get_path("Database/Discount_Bill"),"wb")
    f7 = open(get_path("Database/Coupon Code.dat"),"rb")
    f8 = open(get_path("Database/retail.dat"),"rb")
    ID_Number = pickle.load(f7)
    data = pickle.load(f1)
    data_2 = pickle.load(f2)
    data_3 = pickle.load(f3)
    data_4 = pickle.load(f4)
    data_5 = pickle.load(f5)
    data_8 = pickle.load(f8)
    items = []
    total = sum(data_3)
    for i in data.keys():
        items.append(i)
    total_bill = sum(data_5) - total
    round_fig = round(total_bill,2)
    x = datetime.datetime.now()
    y = x.strftime("%D")
    s = x.strftime("%T")
    z = [f"Date:{y}",f"Savings :RS {round_fig}/-",f"DISCOUNT OFFER : 10% on all items", f"\nTime:{s}\nThank You Visit Again!\n\nTotal Amount:{total}Rs/-"]
    Bill_Table = {
        "Product Name" : items,
        "Net Quantity" : data_4,
        "Retail_Value" : data_8,
        "Mart_Value" : data_2,
        "Total Cost" : data_3,
        f"CUSTOMER ID: {ID_Number}" : z
    }
    print(colorama.Style.BRIGHT + colorama.Fore.RED)
    print(tabulate(Bill_Table, headers="keys", tablefmt="psql"))
    print(colorama.Style.RESET_ALL)
    total = int(total)
    pickle.dump(total,f6)
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()