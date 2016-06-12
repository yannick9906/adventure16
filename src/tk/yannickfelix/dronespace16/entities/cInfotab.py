# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
import random

from tk.yannickfelix.dronespace16.entities.cEntity import Entity
from tk.yannickfelix.jsonNetCode import Filesystem


class Infotab(Entity):
    CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜäöü.,:;-_<>|1234567890!\"$%&/(=){[]}\\?ß+*#'^é"

    stages = []
    cleared = 1

    def __init__(self, stages, cleared, name, commands, globalvars):
        """
        This is a infotab, it has different occurences in the game,
        It contains information, some of them is obfuscated

        @param stages: All Information
        @param cleared: How many stages of information are already cleared
        @param name: The name
        @param commands: The commands you can issue
        @param globalvars: The usual globalvars

        @type stages: str[]
        @type cleared: int
        @type name: str
        @type commands: dict
        @type globalvars: dict
        """
        super().__init__(name, -1, commands, globalvars)
        self.stages = stages
        self.cleared = cleared

    @staticmethod
    def fromDict(globalvars, dict):
        """
        Creates an instance of this class
        @see EntitiesFactory

        @param globalvars: The usual globalvars
        @param dict: The dict from savegame to create this instance from

        @type globalvars: dict
        @type dict: dict

        @return: The created instance
        """
        types = Filesystem.loadFile(globalvars["res_folder"]+"/entities/infotabs.json")
        thistype = types[dict["information"]]
        return Infotab(thistype["stages"], dict["cleared"], dict["name"], thistype["commands"], globalvars)

    def getTextObfuscated(self):
        """
        This method obfuscates the not cleared stages
        @return: The complete text, but with obfuscated parts
        @rtype: str
        """
        text = ""
        for i, stage in enumerate(self.stages):
            if self.cleared >= i+1:
                text += stage
            else:
                for char in stage:
                    if char != "\n":
                        char = self.CHARS[random.randint(0, len(self.CHARS)-1)]
                    text += char
        return text

    def detailedInfo(self):
        """
        Only a wrapper for getTextObfuscated()
        Overrides the superclass method
        @return: The text
        @rtype: str
        """
        return self.getTextObfuscated()
