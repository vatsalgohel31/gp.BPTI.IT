# This is the Test file, it provides user interface to the user !
import pickle
import Database.data_server
import Database.design
import Database.functions
import Data_Storage.check_data
from Database.path_helper import get_path

def run():
    Database.data_server.display_data()
    Database.design.display_design()
    Database.functions.My_Shopping_Cart()
    f1 = open(get_path("Database/total.dat"), "rb")
    data = pickle.load(f1)
    f1.close()
    total_amount = sum(data)
    if total_amount > 10000:
        Database.design.Bill()
    else:
        Database.design.display_design_cart()
        Data_Storage.check_data.write_data()

if __name__ == "__main__":
    run()