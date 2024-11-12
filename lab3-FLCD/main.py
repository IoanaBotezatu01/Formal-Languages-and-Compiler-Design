import os

from MyScanner import MyScanner


def print_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(str(content))
    except FileNotFoundError as e:
        print(f"File not found: {e}")

def run(file_path):
    scanner = MyScanner(file_path)
    scanner.scan()
    st_file_path = file_path.replace(".txt", "ST.txt")
    pif_file_path = file_path.replace(".txt", "PIF.txt")
    print_to_file(st_file_path, scanner.get_symbol_table().get_hash_table())
    print_to_file(pif_file_path, scanner.get_pif())

if __name__ == "__main__":
    run("InOut/p1.txt")
    run("InOut/p2.txt")
    run("InOut/p3.txt")
    run("InOut/p1err.txt")
