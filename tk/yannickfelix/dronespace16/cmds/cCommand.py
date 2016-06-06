# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""


class Command(object):
    hasArgs = False
    command = ""
    action = {}

    def __init__(self, command, action):
        """

        @param command: The Command String
        @param action: The Action to do when cmd is issued

        @type command: str
        @type action: dict
        """
        self.action = action
        if command.__contains__("*"):
            self.command = command.replace("*", "").replace(" ", "")
            self.hasArgs = True
        else:
            self.command = command

    def isThisCommand(self, cmd):
        """

        @param cmd: The Command String to check
        @type cmd: str
        @return: If this Command is this string
        @rtype: bool
        """
        if self.hasArgs:
            cmd = cmd.replace(" ","")
            return cmd.startswith(self.command)
        else:
            return cmd == self.command or cmd.startswith(self.command)