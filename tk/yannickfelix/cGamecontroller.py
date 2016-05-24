"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.tkwrapper import *
from tk.yannickfelix.dronespace import *


class Gamecontroller(object):
    textoutput = None
    textinput = None
    userinput = None

    def __init__(self, textoutput, textinput, userinput):
        """

        @param textoutput: GTextOutput
        @param textinput: GTextInput
        @param userinput: GUserInput
        """
        self.textinput = textinput
        self.textoutput = textoutput
        self.userinput = userinput

    def update(self):
        cmd = self.textinput.getUserText()
        self.textoutput.printMessage(cmd, "right", "")