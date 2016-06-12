
# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.dronespace16.entities.cEntity import Entity


class Door(Entity):

    locked = False
    to = 1

    def __init__(self, to, locked, name, commands, globalvars):
        """
        This class is a door class

        @param to: Where this door goes
        @param locked: If the door is locked
        @param name: The name of this door
        @param commands: The commands you can issue
        @param globalvars: The usual globalvars

        @type to: int
        @type locked: bool
        @type name: str
        @type commands: dict
        @type globalvars: dict
        """
        # -1 is used as id because this is a subentity
        super().__init__(name, -1, commands, globalvars)
        self.locked = locked
        self.to = to

    @staticmethod
    def fromDict(globalvars, dict):
        """
        Creates a door
        @see EntitiesFactory

        @param globalvars: The usual globalvars
        @param dict: the dict used to create a instance

        @type globalvars: dict
        @type dict: dict

        @return: The created instance
        @rtype: Door
        """
        cmds = {}
        return Door(dict["to"], dict["locked"], dict["name"], cmds, globalvars)

