# this file contains the data for displaying it to the main user interface file
import pickle
from Database.path_helper import get_path

def display_data():
    file_0 = open(get_path("Database/database.dat"), "wb")          # database file
    file_1 = open(get_path("Database/chocolate_data.dat"), "rb")    # chocolate file
    file_2 = open(get_path("Database/stationary_data.dat"), "rb")   # stationary file
    file_3 = open(get_path("Database/chocolates_count.dat"),"rb")   # chocolate total count file
    file_4 = open(get_path("Database/stationary_count.dat"),"rb")   # stationary total count file
    file_5 = open(get_path("Database/Product_Number.dat"),"wb")     # Total display count file
    choco_count = pickle.load(file_3)
    stat_count = pickle.load(file_4)
    CHOCO_DATA = pickle.load(file_1)
    STAT_DATA = pickle.load(file_2)
    DATA = dict()
    retailed_value = []
    Product_number = []
    count = 0
    total_count = choco_count + stat_count
    for i in total_count :
        count+=1
        Product_number.append(count)
    for i in CHOCO_DATA,STAT_DATA:
        DATA.update(i)
    for x in DATA.values():
        retailed_value.append(x)
    pickle.dump(DATA,file_0)
    pickle.dump(Product_number,file_5)
    file_0.close()
    file_1.close()
    file_2.close()
    file_3.close()
    file_4.close()
    file_5.close()