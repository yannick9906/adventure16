"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""


class DockingStation(object):
    entityID = 0
    damage = 0
    name = ""
    dockedEntity = 0
    locked = True

    def __init__(self, entityID, damage, name, dockedEntity, locked):
        """

        @param entityID: int
        @param damage: int
        @param name: str
        @param dockedEntity: int
        @param locked: bool
        """
        self.entityID = entityID
        self.damage = damage
        self.name = name
        self.dockedEntity = dockedEntity
        self.locked = locked

    @staticmethod
    def fromDict(id, dict):
        """
        Creates a new DockingStation from giving dict
        @param id: int
        @param dict: dict
        @return: DockingStation
        """
        return DockingStation(id, dict['damage'], dict['name'], dict['dockedEntity'], dict['locked'])
