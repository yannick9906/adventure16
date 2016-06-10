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


class Room(Entity):
    entities = []

    def __init__(self, id, name, commands, globalvars, entities):
        super().__init__(name, id, commands, globalvars)
        self.entities = entities

    @staticmethod
    def fromDict(globalvars, dict):
        return Room(dict['id'], dict["name"], dict["commands"], globalvars, dict['entities'])

    def finishLoad(self):
        temp = []
        for key in self.entities:
            temp.append(self.globalvars["all_entities"][str(key)])
        self.entities = temp

    def getEntities(self):
        list = []
        for entity in self.entities:
            list.append("{0:3.0f}:> {1}".format(entity.id, entity.name))
