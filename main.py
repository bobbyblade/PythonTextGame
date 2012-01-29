# coding: utf-8

from sys import exit
from random import randint
import string
import rooms

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

# Game object, runs the game.
class Game(object):
    def __init__(self):
        self.rooms = [
            rooms.OutsideEntry, # Room 1
            rooms.OutdoorEast, # Room 2
            rooms.OutdoorWest # Room 3
        ]
        self.play()
        
    def play(self):
        while True:
            input = raw_input("> ")
            list = input.split(" ")
            action = list.pop(0)
            self.commands(action, list)
            
    def commands(self,action,args):
        if action == "look":
            self.rooms[player.location-1]().look()
        
        elif action == "peer":
            room = self.rooms[player.location-1]()
            direction = args[0]
            if room.check_exit(direction) != False:
                self.rooms[room.check_exit(direction)-1]().peer()
            else:
                print "Sorry, there is nothing to see in that direction."

        elif action == "east" or action == "west" or action == "north" or action == "south":
            # Player is trying to move, lets see if they are going in a valid direction.
            room = self.rooms[player.location-1]()
            if room.check_exit(action) != False:
                player.location = room.check_exit(action)
                self.rooms[player.location-1]().look()
            else:
                print "Sorry, there is no exit in that direction."
            
        
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
<direction> - attempt to travel in the entered direction
            
Legend:
<direction> may be north, south, east or west
"""
            
        else:
            print "I'm sorry, I don't understand, type `help` to get a list of commands."
# End of Game Class
player = Player()
Game()