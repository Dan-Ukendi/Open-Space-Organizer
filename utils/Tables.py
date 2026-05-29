class Seat:
    '''
    Class that will create a seat with a table and a person asign to it 

    :param number one: Object Table that will be the table of the seat
    :atribut number one: a boolean Free that will say if the seat is taken if False
    :atribut number two: a string wich is the name of the person on the seat
    '''
    def __init__(self, table):
        self.table = table
        self.occupant = None
        self.free = True
    
    def set_occupant(self, occupant):
        '''
        Fuction that will set a occupant on the seat
        :param number one : the name of the occupant of the table
        return: a boolean wich will be false if the seat is taken 
        '''
        self.occupant = occupant
        self.free = False
    
    def remove_occupant(self):
        '''
        Fucntion that will remove a occupant from a seat
        return: a boolean wich is true if the seat has be freed
        '''
        self.occupant = None
        self.free = True

class Table:
    '''
    Class who create a table wich is a array of seat
    param number one: a int that will set the number of seat in a table
    param number two: a int that will set the number of the table
    '''
    def __init__(self, capacity, number):
        self.number = number
        self.seats = []
        for i in range(capacity):
            self.seats.append(Seat(self))   
    
    def has_free_spot(self, seat):
        '''
        Function to know if there is free space in the table on a seat
        param number one: a seat on the table
        '''
        if seat.free:
            return True
        return False
    
    def assign_seat(self, name):
        '''
        Fucntion that will assign a person on a free seat in the table
        param number one: a string with the name of the person to assign 
        '''
        for seat in self.seats:
            if self.has_free_spot(seat):
                seat.set_occupant(name)
                return True
        return False
    def remove_occupant(self, name):
        '''
        Fuction that will free a seat on a table
        param number two: string with the nama of the person to remove from the table
        return: a boolean wich is true if a seat has been freed
        '''
        for seat in self.seats:
            if seat.occupant == name:
                seat.remove_occupant()
                return True
        return False
    def left_capacity(self):
        '''
        Fuction that will tell how many seat are left on the table
        return: the number of free seat on the table
        '''
        count = 0
        for seat in self.seats:
            if seat.free:
                count += 1
        return count

    def move_occupant(self, name, new_table):
        '''
        Fuction that will move a occupant on a new table
        param number one: name of the occupant to move
        param number two: the new table of the occupant
        '''
        seat = None
        for s in self.seats:
            if s.occupant == name:
                seat = s
                break
        if seat:
            if new_table.assign_seat(name):
                seat.remove_occupant()
                return True
        return False