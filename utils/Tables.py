class Seat:
    def __init__(self, table):
        self.table = table
        self.occupant = None
        self.free = True
    
    def set_occupant(self, occupant):
        self.occupant = occupant
        self.free = False
    
    def remove_occupant(self):
        self.occupant = None
        self.free = True

class Table:
    def __init__(self, capacity, number):
        self.number = number
        self.seats = []
        for i in range(capacity):
            self.seats.append(Seat(self))   
    
    def has_free_spot(self, seat):
        if seat.free:
            return True
        return False
    
    def assign_seat(self, name):
        for seat in self.seats:
            if self.has_free_spot(seat):
                seat.set_occupant(name)
                return True
        return False
    
    def left_capacity(self):
        count = 0
        for seat in self.seats:
            if seat.free:
                count += 1
        return count