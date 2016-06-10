
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
        super().__init__(name, -1, commands, globalvars)
        self.locked = locked
        self.to = to

    @staticmethod
    def fromDict(globalvars, dict):
        cmds = {}
        return Door(dict["to"], dict["locked"], dict["name"], cmds, globalvars)

