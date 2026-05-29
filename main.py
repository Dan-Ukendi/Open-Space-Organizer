from utils.openspace import OpenSpace
    
def main():
    '''
    Function that will run the program wich has this following steps:
    1. Ask the user for the path to the file with the names of the collegues, the number of tables and the size of each table
    2. Ask the user if they want to add more person to the list of collegues
    3. Create an OpenSpace object with the number of tables and the size of each table
    4. Check if there are enough seats for all the collegues, if not ask the user if they want to add more tables
    5. Organize the space with the list of collegues and the OpenSpace object
    6. Ask the user if they want to know the number of free seats, the number of people in the room and the number of seats in the room
    7. Ask the user if they want to make sure that nobody is alone in a table, if 2 people can't sit together or if 2 people must sit together
    8. Store the seating arrangement in a txt file and display it
    '''
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
    while ask:
        question = input("Do you want to know the number of free seats? (y/n): ")
        if question == "y":
            print(f"Number of free seats: {space.number_of_free_seats()}")
        elif question == "n":
            ask = False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    ask = True
    while ask:
        question = input("Do you want to know the number of people in the room? (y/n): ")
        if question == "y":
            print(f"Number of people in the room: {len(new_collegues)}")
        elif question == "n":
            ask = False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    
    ask = True
    while ask:
        question = input("Do you want to know the number of seats in the room? (y/n): ")
        if question == "y":
            print(f"Number of seats in the room: {space.total_seats()}")
        elif question == "n":
            ask = False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    space.no_solo()
    ask = True
    while ask:
        question = input("Does 2 people can't sit together? (y/n): ")
        if question == "y":
            name1 = input("Enter the name of the first person: ")
            while not space.check_seat(name1):
                print("Name not found. Please enter a valid name.")
                name1 = input("Enter the name of the first person: ")
            name2 = input("Enter the name of the second person: ")
            while not space.check_seat(name2):
                print("Name not found. Please enter a valid name.")
                name2 = input("Enter the name of the second person: ")
            space.cant_be_together(name1, name2)
        elif question == "n":
            ask = False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    ask = True
    while ask:
        question = input("Do 2 people must sit together? (y/n): ")
        if question == "y":
            name1 = input("Enter the name of the first person: ")
            while not space.check_seat(name1):
                print("Name not found. Please enter a valid name.")
                name1 = input("Enter the name of the first person: ")
            name2 = input("Enter the name of the second person: ")
            while not space.check_seat(name2):
                print("Name not found. Please enter a valid name.")
                name2 = input("Enter the name of the second person: ")
            space.must_be_together(name1, name2)
        elif question == "n":
            ask = False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    space.store_file("seating_arrangement.txt")
    space.display("./seating_arrangement.txt")

main()

        