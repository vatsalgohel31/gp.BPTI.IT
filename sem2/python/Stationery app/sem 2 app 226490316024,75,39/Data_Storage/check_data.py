import pickle
from Database.path_helper import get_path

def write_data():
    sample = open(get_path("Data_Storage/storage.dat"), "rb")
    sample2 = open(get_path("Data_Storage/storage.txt"), "a")
    data = pickle.load(sample)
    items = []
    for x in data.keys():
        items.append(str(x))
    for y in data.values():
        sample2.write("Customer id:")
        sample2.writelines(items)
        sample2.write(" ")
        sample2.write("Info :")
        sample2.writelines(y)
        sample2.write("\n")
    sample.close()
    sample2.close()
