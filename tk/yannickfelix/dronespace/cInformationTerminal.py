"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""


class InformationTerminal(object):
    damage = 0
    locked = True
    unlockItemId = 0
    text = ""

    def __init__(self, damage, locked, unlockItemId, text):
        """
        InformationTerminal Constructor
        @param damage: int
        @param locked: bool
        @param unlockItemId: int
        @param text: str
        """
        self.damage = damage
        self.locked = locked
        self.unlockItemId = unlockItemId
        self.text = text

    @staticmethod
    def fromDict(dict):
        """
        Creates a new InformationTerminal from given dict
        @param dict: dict
        @return: InformationTerminal
        """
        return InformationTerminal(dict['damage'], dict['locked'], dict['unlockItemId'], dict['text'])
