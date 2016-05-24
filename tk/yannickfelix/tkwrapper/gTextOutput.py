"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""

import textwrap
import tkinter.ttk as ttk


class GTextOutput(object):
    text = ""
    showing = 7
    viewx = 40
    viewymax = 40

    label = None

    def __init__(self, master):
        """
        @rtype: GTextOutput
        @param master: object
        """
        self.label = ttk.Label(master=master, font=("Courier", 12), text="Test", anchor="sw", background="red")

    def printMessage(self, text, side, name=""):
        """
        Prints the requested message onto the Label
        @param text: str
        @param side: str
        @param name: str
        """
        nameLength = len(name+"> ")
        lines = textwrap.wrap(text, self.viewx-nameLength)
        if side == "left":
            self.text += name+"> " + lines[0] + "\n"
            lines.pop(0)
            for line in lines:
                self.text += " "*nameLength + line + "\n"
        elif side == "right":
            self.text += (" "*(self.viewx-nameLength-len(lines[0]))) + lines[0] + " <"+ name + "\n"
            lines.pop(0)
            for line in lines:
                lineLength = nameLength + len(line)
                self.text += (" "*(self.viewx-lineLength)) + line + "\n"
        elif side == "center":
            lines = textwrap.wrap(text, self.viewx)
            for line in lines:
                lineLength = len(line)
                self.text += (" " * ((self.viewx - lineLength)//2)) + line + "\n"
        self.text += "\n"
        text = str.split(self.text, "\n")
        self.text = "\n".join(text[-self.viewymax:])
        self.label.config(text=self.text)
