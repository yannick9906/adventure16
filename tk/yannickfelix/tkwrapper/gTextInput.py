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

    def __init__(self, master):
        self.entry = ttk.Entry(master=master)

    def getUserText(self):
        return self.entry.get()

    def clearUserText(self):
        self.entry.config(text="")
