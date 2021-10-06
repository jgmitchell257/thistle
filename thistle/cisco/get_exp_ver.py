from getpass import getpass
import expressway_v1 as exp

def load_file_to_list(filename: str) -> list:
    clean_data = []
    with open(filename, "r") as f:
        raw_data = f.readlines()
        for i in raw_data:
                clean_file_input = i.strip("\n")
                clean_data.append(clean_file_input)
        f.close()
    return clean_data

username = input("Expressway admin user: ")
password = getpass("Expressway admin password: ")
exp_list = load_file_to_list("xway_int_hs.txt")

for i in exp_list:
    server = i
    print(server)
    try:
        exp.Expressway(server, username, password).getSysInfo()
    except:
        print("Connection error")
    