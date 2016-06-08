# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.jsonNetCode import Filesystem
from tk.yannickfelix.dronespace16.actions import *


class StdCommands(object):
    cmds = None
    globalvars = None
    actionhandler = None

    def __init__(self, globalvars):
        """
        This class combines all Standart Commands, which can always be called
        @param globalvars: The usual globalvars dict
        @type globalvars: dict
        """
        self.globalvars = globalvars
        self.cmds = Filesystem.loadFile(globalvars['res_folder'] + "commands/std.json")
        self.actionhandler = ActionHandler(globalvars)

    def handleCommands(self, cmd):
        """
        This method checks if the cmd is a StdCommand and runs the action
        @param cmd: CMD
        @type cmd: str
        @return: Success
        @rtype: bool
        """
        # If autoreload is enabled it reloads the json
        if self.globalvars['autoreload']:
            self.cmds = Filesystem.loadFile(self.globalvars['res_folder'] + "commands/std.json")
        cmd = cmd.lower()
        try:
            self.actionhandler.handleAction(self.cmds[cmd]['action'], self.cmds[cmd])
            return True
        except KeyError:
            return False
