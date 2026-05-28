from importlib.metadata import files
from utils.openspace import OpenSpace
    
def main():
    path = input("Enter the path to the file: ")
    number_of_tables = int(input("Enter the number of tables: "))
    size_of_tables = int(input("Enter the size of each table: "))
    with open(path, "r") as file:
        new_collegues = file.read().splitlines()
    space = OpenSpace(number_of_tables, size_of_tables)
    space.organize(new_collegues)
    space.display(number_of_tables)
main()

        