def read_and_print_file(filepath):
    with open(filepath) as file:
        for line in file.readlines():
            print(line)