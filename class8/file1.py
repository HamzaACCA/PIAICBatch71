# from *Location* *file name* *function name*
# Set and dictionary {}, list and indexing [], function call and tuples ()
# Object oriented program
class House:
    def __init__(self, adrs):
        self.address = adrs
        self.number_of_rooms = 4
        self.number_of_doors = 2

h1 = House("A1")
print (h1.address)
print (h1.number_of_rooms)

h2 = House("A2")
print (h2.address)


