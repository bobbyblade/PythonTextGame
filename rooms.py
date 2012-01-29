# Base room object, for other rooms to inherit from.
class Room(object):
    def __init__(self):
        self.brief = ""
        self.description = ""
        self.exits = {}
        self.room_number = -1
        
    def look(self):
        print self.description
        print
        print "Possible Exits:"
        for k in self.exits:
            print k
        
    def check_exit(self,direction):
        if direction in self.exits:
            return self.exits[direction]
        else:
            return False
        
    def peer(self):
        print self.brief
        
# End of Room class


# Starting room, the north exit is locked.
class OutsideEntry(Room):
    def __init__(self):
        self.room_number = 1
        self.brief = "Outside, almost pitch black."
        self.description = """You are outside in the rain, you are standing just
south of a large cathedral.  There appears to be gates
spanning the perimeter of the cathedral's yard so it
is doubtful there are any other entrances."""
        self.exits = {"north":4,"east":2,"west":3}
# End of OutsideEntry.Room class

# Outdoor area west of starting room.
class OutdoorEast(Room):
    def __init__(self):
        self.room_number = 2
        self.brief = "Outside, almost pitch black."
        self.description = """You traveled east along the gate and don't notice
The wrought iron gate wraps around this area
anything out of the ordinary."""
        self.exits = {"west":1}
# End of OutsideEntry.Room class

# Outdoor area west of starting room.
class OutdoorWest(Room):
    def __init__(self):
        self.room_number = 3
        self.brief = "Outside, almost pitch black."
        self.description = """You traveled west along the gate and don't notice
The wrought iron gate wraps around this area
anything out of the ordinary."""
        self.exits = {"east":1}
# End of OutsideEntry.Room class