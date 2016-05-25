"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.jsonNetCode import *


class Item(object):
    id = 0
    icon = ""
    name = ""
    amount = 0

    def __init__(self, id, amount, name, icon = ""):
        """

        @param id: int
        @param name: str
        @param icon: str
        """
        self.name = name
        self.icon = icon
        self.id = id
        self.amount = amount

    @staticmethod
    def fromDict(dict):
        """
        Creates a specific Item from a dict
        @param dict: dict
        @return: Item
        """
        loader = Filesystem()
        itemDefinitions = loader.loadFile("../../items.json")
        return Item(dict['id'],dict['amount'],itemDefinitions[str(dict['id'])]['name'],itemDefinitions[str(dict['id'])]['icon'])


