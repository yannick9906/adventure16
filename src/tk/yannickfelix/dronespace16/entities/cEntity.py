# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.dronespace16.actions.cEntityActionHandler import EntityActionHandler
from tk.yannickfelix.dronespace16.cmds import CommandFactory


class Entity(object):
    name = ""
    id = 0
    commands = {}
    globalvars = {}
    actionhandler = None

    def __init__(self, name, id, commands, globalvars):
        """
        This is an simple Entity class. It is not used.
        All Entities are subclasses of this one

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
        self.actionhandler = EntityActionHandler(globalvars, self)

    def update(self):
        """
        This method should be called once per frame
        Here it is empty because there's nothing to update
        but it is need for the subclasses to work
        """
        pass

    def handleCMD(self, cmd):
        """
        Handles issued commands
        @param cmd: The Command issued
        @type cmd: str

        @return: success
        @rtype: bool
        """
        cmd = cmd.replace("interact ", "")
        print("Command:" + cmd)
        for command in self.commands:
            if command.isThisCommand(cmd):
                command.runCommand(self.actionhandler)
                return True
        return False

    def detailedInfo(self):
        """
        @return: Long info string
        @rtype: str
        """
        return "Name:  **{0}**\n".format(self.name)

    def getCmds(self):
        """
        Returns all commands
        @return: The commands as strings
        @rtype: str[]
        """
        list = []
        for command in self.commands:
            list.append(command.command)
        list.sort()
        return list
