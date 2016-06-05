# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from yannickfelix.jsonNetCode import Filesystem
from yannickfelix.dronespace16.entities import *


class EntitiesController(object):
    globalvars = {}
    entities = []
    ships = []

    def __init__(self, globalvars):
        self.globalvars = globalvars
        self.load()

    def load(self):
        savegame = Filesystem.loadFile("../../savegame.json")
        self.entities = EntitiesFactory(self.globalvars).getList(savegame['entities'])

    def handleCommands(self, cmd):
        if cmd == "drones":
            for e in self.entities:
                drone = str(e.getID()) + ": " + e.getName()
                self.globalvars['class_gconsole'].printMessage(drone, "left")
            return True
        return False
