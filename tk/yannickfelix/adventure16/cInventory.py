from tk.yannickfelix.adventure16.cItem import Item


class Inventory(object):
    items = []
    
    def __init__(self):
        """

        :rtype: Inventory
        """
        pass
    
    def addItem(self, item, slot):
        """
        Adds an Itemobject to this Inventory
        :param slot: int
        :param item: Item
        :rtype: bool
        """
        pass

    def removeItem(self, item: Item):
        """
        Removes an Itemobject from this Inventory
        :param item: Item
        :rtype: bool
        """
        pass

    def removeItemFromSlot(self, slot):
        """
        Removes an Itemobject from this Inventory
        :param slot: int
        :rtype: bool
        """
        pass

    def isItemInInventory(self, item):
        """
        Checks if an Itemobject is in this inventory
        :param item: Item
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
        :param slot: int
        :return:
        """
        return self.items[slot]

    def moveItem(self, item, to):
        """
        Moves an Item from this Inventory to another
        :param item: Item
        :param to: Inventory
        """
        pass