"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""

from tk.yannickfelix.tkwrapper.gTextInput import *
from tk.yannickfelix.tkwrapper.gTextOutput import *
from tk.yannickfelix.tkwrapper.gUserInput import *


class GWindow(object):
    textoutput = None
    textinput = None
    userinput = None
    quitButton = None
    window = None
    mainFrame = None

    def __init__(self, title: str="A Game Window"):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry("800x600")
        self.mainFrame = ttk.Frame(master=self.window)
        self.mainFrame.place(x=0, y=0, width=800, height=600)
        self.textoutput = GTextOutput(master=self.mainFrame)
        self.textoutput.label.place(x=0, y=0, width=402, height=600)
        self.textinput = GTextInput(master=self.mainFrame)
        self.textinput.entry.place(x=0, y=601, width=402, height=0)
        self.userinput = GUserInput(master=self.mainFrame)
        self.userinput.position.place(x=402, y=520, width=398, height=80)



