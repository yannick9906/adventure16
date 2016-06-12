# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.jsonNetCode import Filesystem
from .cEntity import *


class ChargingPot(Entity):

    def __init__(self, name, id, commands, globalvars):
        """

        @param name: The name of this Entity
        @param id: The Entities ID
        @param commands: The raw commands
        @param globalvars: The usual globalvars

        @type name: str
        @type id: int
        @type commands: dict
        @type globalvars: dict
        """
        super().__init__(name, id, commands, globalvars)


    @staticmethod
    def fromDict(globalvars, dict):
        """
        Creates an instance of this class
        @see EntitiesFactory

        @param globalvars: The usual globalvars
        @param dict: The dict from savegame to create this instance from

        @type globalvars: dict
        @type dict: dict

        @return: The created instance
        """
        type = Filesystem.loadFile(globalvars["res_folder"] + "/entities/chargingpot.json")
        return ChargingPot(dict["name"], -1, type["commands"], globalvars)