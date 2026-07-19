# this file contains all the functions
import pickle, colorama
import random,math
from Database import design
from Database.path_helper import get_path

MY_CART = dict()
Net_quantity = []
retail_price = []
Total = []
Update_net = []
Update_total = []
OUR_VALUE = []
OUR_TOTAL = []
BILL = dict()

def Coupon_discount():
    file = open(get_path("Database/code_cheats.dat"),"wb")
    Discount_Code = {"-": 95, "BPTI10" : 90, "BPTI20" : 80, "BPTI30": 70, "BPTI08" : 92}
    pickle.dump(Discount_Code,file)
    file.close()

def generate_id():
    f1 = open(get_path("Database/Coupon Code.dat"),"wb")
    digits = "0123456789ABCDEFGHIJKLMNOPQURSTUVWKVZ"
    len_digi = len(digits)
    coupon_code = " "
    for i in range(6):
        coupon_code += digits[math.floor(random.random() * len_digi)]
    pickle.dump(coupon_code,f1)
    f1.close()

def buy():
    generate_id()
    f1 = open(get_path("Database/database.dat"), "rb")
    f2 = open(get_path("Database/Product_Number.dat"), "rb")
    f3 = open(get_path("Database/total.dat"), "wb")
    f4 = open(get_path("Database/retail.dat"), "wb")
    f5 = open(get_path("Database/net_quantity.dat"), "wb")
    f6 = open(get_path("Database/My_Shopping_Cart.dat"), "wb")
    f7 = open(get_path("Database/Mart_Value.dat"),"wb")
    f8 = open(get_path("Database/Mart_Total.dat"),"wb")
    f9 = open(get_path("Database/Mart_Bill.dat"),"wb")
    Mart_Value = 90
    count = 0
    data = pickle.load(f1)
    count_list = pickle.load(f2)
    n = input("enter the Product Number that you want to buy !:")
    Product_number = int(n)
    for x in data.keys():
        count += 1
        if Product_number == count:
            net_quantity = int(input(f"How many {x} do you want !:"))
            print(colorama.Style.NORMAL + colorama.Fore.BLUE +f"{x} Successfully added in your cart")
            print(colorama.Style.RESET_ALL)
            retail = data.get(x)
            Mart_Discount = data.get(x) * Mart_Value/100
            total = net_quantity * retail
            Dis_Total = net_quantity * Mart_Discount
            if total == 0 or Dis_Total == 0:
                break
            OUR_VALUE.append(Mart_Discount)
            OUR_TOTAL.append(Dis_Total)
            Net_quantity.append(net_quantity)
            retail_price.append(retail)
            Total.append(total)
            BILL[x] = [net_quantity,OUR_TOTAL]
            MY_CART[x] = [net_quantity,total]
        if Product_number > count_list[-1]:
            print("The item isn't available !")
            break
    pickle.dump(Total, f3)
    pickle.dump(retail_price, f4)
    pickle.dump(Net_quantity, f5)
    pickle.dump(MY_CART, f6)
    pickle.dump(OUR_VALUE, f7)
    pickle.dump(OUR_TOTAL, f8)
    pickle.dump(BILL,f9)
    MY_CART.update()
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
    f9.close()

def sort():
    design.sort_design()
    user = input("Select the Category\nPress Function Key :")
    if user == "c" or user == "C":
        design.display_chocolate()
    if user == "s" or user == "S" :
        design.display_stationary()

def My_Shopping_Cart():
    design.display_function()
    while True :
        Function = input(">>>Enter Function Key To access the Functionality of our Market Place\nPress Key here :")
        if Function == "r" or Function == "R":
            budget()
            design.budget_design()
        elif Function == "f" or Function == "F":
            find()
        elif Function == "b" or Function == "B":
            buy()
        elif Function == "q" or Function == "Q":
            break
        elif Function == "s" or Function == "S":
            sort()
            user = input("Do You want to buy an item(Y/N) :")
            if user == "y" or user == "Y":
                buy()
            else :
                continue
        elif Function == "h" or Function == "H":
            print(colorama.Fore.RED + colorama.Style.BRIGHT +"Here is the list of function\nYou can use this Function by pressing the Function-Key\nPress Q key to exit!")
            print(colorama.Style.RESET_ALL)
            design.display_function()
        else:
            print(colorama.Fore.RED + "Invalid Key! Please enter a valid Function Key (S, R, F, B, H, Q)." + colorama.Style.RESET_ALL)

def budget():
    f1 = open(get_path("Database/database.dat"),"rb")
    f3 = open(get_path("Database/Budget_Range.dat"),"wb")
    range = dict()
    data = pickle.load(f1)
    user = input("Enter your Budget Range:")
    user = int(user)
    for x in data.keys():
        y = data.get(x)
        if y <= user :
            range[x] = y
    pickle.dump(range,f3)
    f1.close()
    f3.close()

def find():
    f1 = open(get_path("Database/database.dat"), "rb")
    data = pickle.load(f1)
    f1.close()
    count = 0
    user = input("Enter the item name that you want to find!:")
    print("Are you Searching For!:")
    for x in data.keys():
        count+=1
        if user[0:5:1] in x[::] :
            print(colorama.Style.BRIGHT + colorama.Fore.LIGHTMAGENTA_EX + f"Product Name:{x}, Product Number:{count}")
            print(colorama.Style.RESET_ALL)