"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from yannickfelix.jsonNetCode import Filesystem


class StdCommands(object):
    cmds = None
    globalvars = None

    def __init__(self, globalvars):
        self.globalvars = globalvars
        self.cmds = Filesystem.loadFile(globalvars['res_folder'] + "commands/std.json")

    def handleCommands(self, cmd):
        cmd = cmd.lower()
        try:
            self.globalvars['class_actioncontroller'].handleAction(self.cmds[cmd]['action'], self.cmds[cmd])
            return True
        except KeyError:
            return False
