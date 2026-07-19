# this file contains functions for getting the data  !
import pickle
from Database.path_helper import get_path

CHOCO = dict()
STAT = dict()

def get_data_chocolates():
    f1 = open(get_path("Database/chocolate_data.dat"),"wb")
    f2 = open(get_path("Database/chocolates_count.dat"),"wb")
    count = 0
    count_list =[]
    while True:
        count+=1
        count_list.append(count)
        Product = input("enter the product name:")
        while True:
            rate = input(f"enter the rate of {Product} in Rs/-")
            if rate.isdigit():
                rate = int(rate)
                if rate >= 0:
                    break
                else:
                    print("Error:Enter Positive Value")
            else:
                print("Error:Enter valid input")
        CHOCO[Product] = rate
        CHOCO.update()
        quit = input("enter q to exit")
        if quit == "q":
            break
    pickle.dump(CHOCO, f1)
    pickle.dump(count_list,f2)
    f1.close()
    f2.close()

def get_data_stationary():
    f1 = open(get_path("Database/stationary_data.dat"),"wb")
    f2 = open(get_path("Database/stationary_count.dat"),"wb")
    count = 0
    count_list = []
    while True:
        count+=1
        count_list.append(count)
        Product = input("enter the product name:")
        while True:
            rate = input(f"enter the rate of {Product} in Rs/-")
            if rate.isdigit():
                rate = int(rate)
                if rate >= 0:
                    break
                else:
                    print("Error:Enter Positive Value")
            else:
                print("Error:Enter valid input")
        STAT[Product] = rate
        STAT.update()
        quit = input("enter q to exit")
        if quit == "q":
            break
    pickle.dump(STAT, f1)
    pickle.dump(count_list,f2)
    f1.close()
    f2.close()

