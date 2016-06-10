# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.dronespace16.entities import *
from tk.yannickfelix.dronespace16.entities.cEntity import *


class Room(Entity):
    entities = []

    def __init__(self, id, name, commands, globalvars, entities):
        super().__init__(name, id, commands, globalvars)

        from . import EntitiesFactory
        self.entities = EntitiesFactory(globalvars).getList(entities)

    @staticmethod
    def fromDict(globalvars, id, dict):
        return Room(id, dict["name"], dict["commands"], globalvars, dict['entities'])

    def finishLoad(self):
        temp = []
        for key in self.entities:
            temp.append(self.globalvars["all_entities"][str(key)])
        self.entities = temp

    def getEntities(self):
        return self.entities

    def getEntity(self, id):
        try:
            return self.entities[id]
        except IndexError:
            return None