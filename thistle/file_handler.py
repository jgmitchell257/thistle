def load_file_to_list(filename: str) -> list:
    with open(filename, "r") as f:
        file_data = f.readlines()
        return file_data