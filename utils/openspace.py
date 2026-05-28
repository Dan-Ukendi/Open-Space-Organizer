import random
from .Tables import Table

class OpenSpace :
    def __init__(self, number_of_tables, size_of_tables):
        self.tables = []
        for i in range(number_of_tables):
            self.tables.append(Table(size_of_tables, i))
    def organize(self, names):
        shuffled_names = names[:]
        random.shuffle(shuffled_names)
        for name in shuffled_names:
            assigned = False
            for table in self.tables:
                if table.assign_seat(name):
                    assigned = True
                    break
            if not assigned:
                print(f"No more seats available for {name}.")
        count = 0
        for table in self.tables:
                count += table.left_capacity()
        print(f"Total free seats left: {count}")
    def display(self, number_of_tables):
        for i in range(number_of_tables):
            print(f"Table {i}:")
            for seat in self.tables[i].seats:
                if seat.free:
                    print("  - Free")
                else:
                    print(f"  - {seat.occupant}")