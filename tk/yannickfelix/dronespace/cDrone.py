"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.dronespace.cInventory import *


class Drone(object):
    entityID = 0
    name = ""
    type = ""
    inventory = None
    energy = 0
    printText = None
    commands = {}

    def __init__(self, entityID, name, type, inventory, energy, printText):
        """
        Drone Constructor
        @param entityID: int
        @param name: str
        @param type: str
        @param inventory: dict
        @param energy: float
        """
        self.entityID = entityID
        self.name = name
        self.type = type
        self.inventory = Inventory.fromDict(inventory)
        self.energy = energy
        self.printText = printText
        self.commands = {
            "self": self.comHelp
        }

    @staticmethod
    def fromDict(id, dict, printText):
        """
        Creates a new Drone object from given dict
        @param id: int
        @param dict: dict
        @return: Drone
        """
        return Drone(id, dict['name'], dict['type'], dict['inventory'], dict['energy'], printText)

    def comHelp(self):
        self.printText("Hi I'm "+self.name+". My Type is <"+self.type+"> and I'd like to do what you command me to do.", "left", self.name)

    def runCommand(self, cmd):
        try:
            self.commands[cmd]()
        except:
            return -1