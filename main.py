# coding: utf-8

from sys import exit
from random import randint
import string

# Map
# ▓ ▓ ▓ ▓ ▓
# ▓ ▓ ▓ ▓ ▓
# ▓ ▓ ▓ ▓ ▓
# ▓ ▓ ▓ ▓ ▓
# ▓ ▓ ▓ ▓ ▓
# ▓ ▓ ░ ▓ ▓ 
#
# ▓ 178 nothing
# ▒ 177 occupied room
# ░ 176 empty room

# Player object, will hold player data.
class Player(object):
    def __init__(self):
        self.inventory = []
        self.location = 1
        self.life = 10
# End of Player class

# Base mob object, for other mobs to inherit from.
class Mob(object):
    def __init__(self):
        self.name = ""
        self.description = ""
        self.defeat = []
        self.alive = 1
        self.location = -1
        
    # Mobs are defeated by submitting text to them.
    def ask(self,answer):
        for death in self.defeat:
            if answer.lower() == death.lower():
                self.alive = 0
                print "Congratulations!  You have slain the evil %s." % self.name
                return true
        print "%s does not like your tone and has struck you!" % self.name
        return false
# End of Mob class
    

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

# Game object, runs the game.
class Game(object):
    def __init__(self):
        self.rooms = [
            OutsideEntry
        ]
        self.play()
        
    def play(self):
        while True:
            input = raw_input("> ")
            list = input.split(" ")
            action = list.pop(0)
            self.commands(action, list)
            
    def commands(self,action,*args):
        if action == "look":
            room = self.rooms[player.location-1]()
            print OutsideEntry().look()
        
        elif action == "peer":
            print args
        
        elif action == "exit":
            print "Okay, see you later!"
            exit(0);
            
        elif action == "help":
            print """
Here is a list of available commands:
            
help - displays this list of commands
look - looks at the room you are currently in:
peer <direction> - takes a quick glance in that direction
exit - exits the game, progress is not saved
inventory - lists the items currently in your inventory
use <inventory> - use an item from your inventory
answer <answer> - answering riddles is how you beat mobs
            
Legend:
<direction> may be north, south, east or west
"""
            
        else:
            print "I'm sorry, I don't understand, type `help` to get a list of commands."
# End of Game Class
OutsideEntry().look()
player = Player()
Game()