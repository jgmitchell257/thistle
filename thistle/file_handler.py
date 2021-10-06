def load_file_to_list(filename: str) -> list:
    clean_data = []
    with open(filename, "r") as f:
        raw_data = f.readlines()
        for i in raw_data:
                clean_file_input = i.strip("\n")
                clean_data.append(clean_file_input)
        f.close()
    return clean_data