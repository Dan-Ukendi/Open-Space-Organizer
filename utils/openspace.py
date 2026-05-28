import random
from .Tables import Table

class OpenSpace :
    def __init__(self, number_of_tables, size_of_tables):
        self.tables = []
        self.number_of_tables = number_of_tables
        self.size_of_tables = size_of_tables
        for i in range(self.number_of_tables):
            self.tables.append(Table(self.size_of_tables, i))
    
    def organize(self, names):
        shuffled_names = names[:]
        random.shuffle(shuffled_names)
        i = 0
        p = 0
        for i in range(len(shuffled_names)):
            name = shuffled_names[i]
            assigned = False
            for p in range(len(self.tables)):
                table = self.tables[p]
                if ((len(shuffled_names) - i) == 3) and (table.left_capacity() < 2):
                    continue
                if table.assign_seat(name):
                    assigned = True
                    break
            if not assigned:
                print(f"No more seats available for {name}.")
    def display(self, path):
        with open(path, "r") as file:
            seating_arrangement = file.read()
        print(seating_arrangement)
    
    def store_file(self, files_name):
        with open(files_name, "w") as file:
            for table in self.tables:
                for seat in table.seats:
                    if not seat.free:
                        file.write(f"{seat.occupant}, Table {table.number}\n")
    
    def number_of_free_seats(self):
        count = 0
        for table in self.tables:
            for seat in table.seats:
                if seat.free:
                    count += 1
        return count
    def add_tables(self, number_of_tables):
        self.number_of_tables += number_of_tables
        self.tables = []
        for i in range(self.number_of_tables):
            self.tables.append(Table(self.size_of_tables, i))
    
    def total_seats(self):
        return self.number_of_tables * self.size_of_tables