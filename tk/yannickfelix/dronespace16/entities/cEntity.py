# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from yannickfelix.dronespace16.cmds import CommandFactory


class Entity(object):
    name = ""
    id = 0
    commands = {}
    globalvars = {}

    def __init__(self, name, id, commands, globalvars):
        """
        Entity Constructor
        @param name: The name of this Entity
        @param id: The Entities ID
        @param commands: The raw commands
        @param globalvars: The usual globalvars

        @type name: str
        @type id: int
        @type commands: dict
        @type globalvars: dict
        """
        self.id = id
        self.name = name
        self.globalvars = globalvars
        self.commands = CommandFactory().listOCommands(commands)

    # TODO make methods O.o
