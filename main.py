from sys import exit
from random import randint

# Player object, will hold player data.
class Player(object):
    def __init__(self):
        self.inventory = []
        self.location = 0
        self.life = 10
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
    
    

# Base room object, for other rooms to inherit from.
class Room(object):
    def __init__(self):
        self.brief = ""
        self.description = ""
        self.exits = []
        
    def look(self):
        print self.description
        print "Possible Exits:"
        for exit in self.exits:
            print exit
        
    def peer(self):
        print self.brief
    

# Game object, runs the game.
class Game(object):
    
    def __init__(self,player,):
        self.r = "> "
        self.rooms = [
            "OutsideEntry"
        ]
    
    def play(self):
        