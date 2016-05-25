"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""

from tk.yannickfelix.dronespace.cItem import *


class Inventory(object):
    items = []
    size = 0

    def __init__(self, items, size=5):
        """


        @param items: list
        @param size: int
        """
        for item in items:
            self.items.append(Item.fromDict(item))
        self.size = size

    @staticmethod
    def fromDict(dict):
        return Inventory(dict['items'], dict['size'])

    def addItem(self, item, slot):
        """
        Adds an Itemobject to this Inventory
        @param slot: int
        @param item: Item
        :rtype: bool
        """
        pass

    def removeItem(self, item: Item):
        """
        Removes an Itemobject from this Inventory
        @param item: Item
        :rtype: bool
        """
        pass

    def removeItemFromSlot(self, slot):
        """
        Removes an Itemobject from this Inventory
        @param slot: int
        :rtype: bool
        """
        pass

    def isItemInInventory(self, item):
        """
        Checks if an Itemobject is in this inventory
        @param item: Item
        :rtype: bool
        """
        pass

    def getNextEmptySlot(self):
        """
        Returns the next slot id where a item can be inserted
        :rtype: int
        """
        pass

    def getSlotForItem(self, item):
        pass

    def getSlot(self, slot):
        """
        Returns the Itemobject currently in this slot
        :rtype: Item[]
        @param slot: int
        :return:
        """
        return self.items[slot]

    def moveItem(self, item, to):
        """
        Moves an Item from this Inventory to another
        @param item: Item
        @param to: Inventory
        """
        pass
