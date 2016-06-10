# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from . import *
from .drones import *
from .cRoom import *
from .cInfotab import *


class EntitiesFactory(object):
    globalvars = {}

    def __init__(self, globalvars):
        """
        @type globalvars: dict
        """
        self.globalvars = globalvars

    def get(self, ID, dict):
        """
        Creates an entity from savegame
        @param ID: the entity id
        @param dict: the data

        @type ID: int
        @type dict: dict

        @return: The Entity
        @rtype: object
        """
        type = dict['type']
        if type == "drone":
            return DroneFactory(self.globalvars).getDrone(ID, dict)
        elif type == "room":
            return Room.fromDict(self.globalvars, ID, dict)
        elif type == "infotab":
            return Infotab.fromDict(self.globalvars, dict)
        elif type == "ship":
            pass

    def getList(self, dict):
        """
        Creates all entities in this list
        @see get()

        @param dict: The list with the entities data and ids
        @type dict: dict

        @return: A list with entities
        @rtype: list
        """
        list = []
        for key, elem in enumerate(dict):
            list.append(self.get(key, elem))
        return list
