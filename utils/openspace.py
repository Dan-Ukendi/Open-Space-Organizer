import random
from .Tables import Table

class OpenSpace :
    '''
    Class that represent a open space wich is a array of tables
    param nummber one: a int wich is the number of tables in the space
    param number two: a int wich is the size of each tables
    '''
    def __init__(self, number_of_tables, size_of_tables):
        self.tables = []
        self.number_of_tables = number_of_tables
        self.size_of_tables = size_of_tables
        for i in range(self.number_of_tables):
            self.tables.append(Table(self.size_of_tables, i))
    
    def organize(self, names):
        '''
        Fuction that will assign a seat to each person on the list of people given
        param number one: a list of string in wich are the name of the people in the room
        '''
        shuffled_names = names[:]
        random.shuffle(shuffled_names)
        i = 0
        p = 0
        for i in range(len(shuffled_names)):
            name = shuffled_names[i]
            assigned = False
            for p in range(len(self.tables)):
                table = self.tables[p]
                if table.assign_seat(name):
                    assigned = True
                    break
            if not assigned:
                print(f"No more seats available for {name}.")
    
    def display(self, path):
        '''
        Fuction that will display the place of each person in the room
        param number one: a path to a txt files with seating arrangement
        '''
        with open(path, "r") as file:
            seating_arrangement = file.read()
        print(seating_arrangement)
    
    def store_file(self, files_name):
        '''
        Fuction that will store the seating arrangement in a txt files
        param number one: the name of the files of seating arrangement
        '''
        with open(files_name, "w") as file:
            for table in self.tables:
                for seat in table.seats:
                    if not seat.free:
                        file.write(f"{seat.occupant}, Table {table.number}\n")
    
    def number_of_free_seats(self):
        '''
        Fuction that will count the number of free seat 
        return: int wich is the number of free seat
        '''
        count = 0
        for table in self.tables:
            for seat in table.seats:
                if seat.free:
                    count += 1
        return count
    def add_tables(self, number_of_tables):
        '''
        Function that will add a tables to the space
        param number one: the number of tables to add
        '''
        self.number_of_tables += number_of_tables
        self.tables = []
        for i in range(self.number_of_tables):
            self.tables.append(Table(self.size_of_tables, i))
    
    def total_seats(self):
        '''
        Fuction that count the number of seat in the space
        return: number of seat in the space
        '''
        return self.number_of_tables * self.size_of_tables
    
    def no_solo(self):
        '''
        Function that will make sure that nobody is alone in a table
        '''
        i = 0
        for i in range(len(self.tables)):
            table = self.tables[i]
            if table.left_capacity() == self.size_of_tables - 1:
                self.tables[i].move_occupant(self.tables[i-1].seats[0].occupant, self.tables[i])
                return True
        return False
    
    def switch_seats(self,name1,name2):
        '''
        Function that switch the seat of two occupant
        param number one: name of the first occupant
        param number two: name of the second occupant
        '''
        seat1 = None
        seat2 = None
        for table in self.tables:
            for seat in table.seats:
                if seat.occupant == name1:
                    seat1 = seat
                elif seat.occupant == name2:
                    seat2 = seat
        if seat1 and seat2:
            occupant1 = seat1.occupant
            occupant2 = seat2.occupant
            seat1.set_occupant(occupant2)
            seat2.set_occupant(occupant1)
            return True
        return False
    
    def cant_be_together(self,name1,name2):
        '''
        Fuction that will make sure that two people can't sit together
        param number one: name of the first person
        param number two: name of the second person
        '''
        seat1 = None
        seat2 = None
        for table in self.tables:
            for seat in table.seats:
                if seat.occupant == name1:
                    seat1 = seat
                elif seat.occupant == name2:
                    seat2 = seat
        if seat1 and seat2:
            if seat1.table == seat2.table:
                i = 0
                for i in range(len(self.tables)):
                    if self.tables[i] != table:
                        self.switch_seats(name2,self.tables[i].seats[0].occupant)
                        return True
        return False
    
    def must_be_together(self,name1,name2):
        '''
        Function that will make sure that two people must sit together
        param number one: name of the first person
        param number two: name of the second person
        '''
        seat1 = None
        seat2 = None
        for table in self.tables:
            for seat in table.seats:
                if seat.occupant == name1:
                    seat1 = seat
                elif seat.occupant == name2:
                    seat2 = seat
        if seat1 and seat2:
            if seat1.table != seat2.table:
                self.switch_seats(name2,seat1.table.seats[0].occupant)
                return True
        return False
    
    def check_seat(self,name):
        '''
        Fuction that will check if a person is in the space
        param number one: name of the person to check
        return: a boolean wich is true if the person is in the space
        '''
        for table in self.tables:
            for seat in table.seats:
                if seat.occupant == name:
                    return True
        return False