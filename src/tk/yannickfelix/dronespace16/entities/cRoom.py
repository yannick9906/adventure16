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
        """

        @param id: The rooms ID
        @param name: The name of the room
        @param commands: The commands you can issue
        @param globalvars: The usual globalvars
        @param entities: The subentities this room has

        @type id: int
        @type name: str
        @type commands: dict
        @type globalvars: dict
        @type entities: dict
        """
        super().__init__(name, id, commands, globalvars)

        from . import EntitiesFactory
        self.entities = EntitiesFactory(globalvars).getList(entities)

    @staticmethod
    def fromDict(globalvars, id, dict):
        """
        Creates a instance from this class
        @see EntitiesFactory

        @param globalvars: The usual globalvars
        @param id: The entity id
        @param dict: The dict to create this instance from

        @type globalvars: dict
        @type id: int
        @type dict: dict

        @return: The instance created
        @rtype: Room
        """
        return Room(id, dict["name"], dict["commands"], globalvars, dict['entities'])

    def getEntities(self):
        """
        Getter for Entities
        @return: A list with entities
        @rtype: Entity[]
        """
        return self.entities

    def getEntity(self, id):
        """
        Gets a specific subentity
        @param id: The subentities ID
        @type id: int

        @return: The Entity requested
        @rtype: Entity
        """
        try:
            if id >= 0:
                return self.entities[id]
            return None
        except IndexError:
            return None
