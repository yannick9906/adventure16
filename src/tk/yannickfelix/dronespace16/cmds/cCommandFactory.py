# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from .cCommand import *


class CommandFactory(object):

    def __init__(self):
        pass

    def getCommand(self, cmd, dict):
        """
        This method creates a new Command instance
        @param cmd: The Name of the command
        @param dict: The action

        @type cmd: str
        @type dict: dict

        @return: The instance of the Command class
        @rtype: Command
        """
        return Command(cmd, dict)

    def listOCommands(self, dict):
        """
        This method can take a dict of commands and actions and turn them into instances
        @param dict: The Commandnames and actions
        @type dict: dict

        @return: A list of Command instances
        @rtype: Command[]
        """
        if dict.__len__() != 0:
            list = []
            for key, value in dict.items():
                list.append(self.getCommand(key, value))
            return list
        else: return []
