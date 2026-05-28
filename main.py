from importlib.metadata import files
from utils.openspace import OpenSpace
from utils.Tables import Table
    
def main():
    ask = True

    path = input("Enter the path to the file: ")
    number_of_tables = int(input("Enter the number of tables: "))
    size_of_tables = int(input("Enter the size of each table: "))
    with open(path, "r") as file:
        new_collegues = file.read().splitlines()
    while ask:
        response = input("Do you want to add more person? (y/n): ")
        if response == "y":
            name = input("Enter the name to add: ")
            new_collegues.append(name)
        elif response == "n":
            ask = False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    space = OpenSpace(number_of_tables, size_of_tables)
    if space.number_of_free_seats() < len(new_collegues):
        print("Not enough seats for all the collegues.")
        ask = True
        while ask:
            response = input("Do you want to add more tables? (y/n): ")
            if response == "y":
                additional_tables = int(input("Enter the number of additional tables: "))
                space.add_tables(additional_tables)
                ask = False
            elif response == "n":
                print("Proceeding with the current number of tables.")
                ask = False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    space.organize(new_collegues)
    ask = True
    question = input("Do you want to know the number of free seats? (y/n): ")
    if question == "y":
        print(f"Number of free seats: {space.number_of_free_seats()}")
    elif question == "n":
        ask = False
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
    ask = True
    question = input("Do you want to know the number of people in the room? (y/n): ")
    if question == "y":
        print(f"Number of people in the room: {len(new_collegues)}")
    elif question == "n":
        ask = False
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
    ask = True
    question = input("Do you want to know the number of seats in the room? (y/n): ")
    if question == "y":
        print(f"Number of seats in the room: {space.total_seats()}")
    elif question == "n":
        ask = False
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
    space.store_file("seating_arrangement.txt")
    space.display("./seating_arrangement.txt")

main()

        