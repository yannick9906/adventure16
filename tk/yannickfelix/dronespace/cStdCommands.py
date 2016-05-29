"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.jsonNetCode.cFilesystem import *


class StdCommands(object):

    commands = {}
    globalvars = {} # This is an reference to a dict with all global vars needed

    def __init__(self, globalvars):
        self.globalvars = globalvars
        self.globalvars['autoreload'] = False
        self.commands = Filesystem.loadFile("../../std.json")

    def handleCommand(self, cmd):
        if self.globalvars['autoreload']:
            self.commands = Filesystem.loadFile("../../std.json")
        if cmd != '':
            try:
                cmd = self.commands[cmd.lower()]

                if cmd['action'] == "close":
                    self.globalvars['running'] = False
                elif cmd['action'] == "fullscreen":
                    self.globalvars['fullscreen'] = not self.globalvars['fullscreen']
                elif cmd['action'] == "varset":
                    self.globalvars[cmd['var']] = cmd['value']
                elif cmd['action'] == "print":
                    self.globalvars['class_textoutput'].printMessage(cmd['text'], cmd['args'][0], cmd['args'][1], cmd['args'][2])
            except KeyError:
                self.globalvars['class_textoutput'].printMessage("Sorry, I think you misspelled this command... Maybe a cookie would help...","left","")