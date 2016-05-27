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
import tkinter as tk
from tkinter.font import Font

class GTextOutput(object):
    text = ""
    showing = 7
    viewx = 36
    viewymax = 40
    font = "JoystixMonospace-Regular"

    label = None

    def __init__(self, master):
        """
        @rtype: GTextOutput
        @param master: object
        """
        self.label = tk.Text(master=master, font=(self.font, 10), background="black", fg="#18F500")
        self.label.tag_configure("TEST", font=(self.font, 10, "bold"))

    def printMessage(self, text, side, name=""):
        """
        Prints the requested message onto the Label
        @param text: str
        @param side: str
        @param name: str
        """
        self.text = ""
        if text != "":
            nameLength = len(name+"> ")
            lines = textwrap.wrap(text, self.viewx-nameLength-(nameLength*0.1))
            if side == "left":
                self.text += name+"> " + lines[0] + "\n"
                lines.pop(0)
                lines = textwrap.wrap(" ".join(lines), self.viewx)
                for line in lines:
                    self.text += line + "\n"
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
            self.label.insert(tk.END, self.text)
            if side == "left": self.highlight_pattern(name+">", "TEST")
            elif side == "right": self.highlight_pattern("<"+name, "TEST")

    def highlight_pattern(self, pattern, tag, start="1.0", end="end", regexp=False):
        """
         the given tag to all text that matches the given pattern

        If 'regexp' is set to True, pattern will be treated as a regular
        expression according to Tcl's regular expression syntax.
        """

        start = self.label.index(start)
        end = self.label.index(end)
        self.label.mark_set("matchStart", start)
        self.label.mark_set("matchEnd", start)
        self.label.mark_set("searchLimit", end)

        count = tk.IntVar()
        while True:
            index = self.label.search(pattern, "matchEnd", "searchLimit", count=count, regexp=regexp)
            if index == "": break
            if count.get() == 0: break  # degenerate pattern which matches zero-length strings
            self.label.mark_set("matchStart", index)
            self.label.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.label.tag_add(tag, "matchStart", "matchEnd")