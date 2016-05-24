"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""

import tkinter as tk
import tkinter.ttk as ttk


class GTextInput(object):
    entry = None
    lastString = ""

    def __init__(self, master):
        self.entry = ttk.Entry(master=master)
        self.entry.bind("<Return>", self.onEnterUp)

    def getUserText(self):
        string = self.lastString
        self.lastString = ""
        return string

    def onEnterUp(self, event=None):
        self.lastString = self.entry.get()
        self.clearUserText()

    def clearUserText(self):
        self.entry.delete(0, 'end')