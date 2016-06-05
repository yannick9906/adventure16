# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""


class Room(object):
    id = 0
    doors = []
    tileEntities = []
    globalvars = {}

    def __init__(self, globalvars, id, doors, tileEntities):
        self.id = id
        self.globalvars = globalvars
    # TODO Entities and doors

    def fromDict(self, globalvars, dict):
        return Room(globalvars, dict['id'], dict['doors'], dict['tileEntities'])