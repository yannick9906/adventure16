"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from random import randint

import time

from tk.yannickfelix.tkwrapper import *
from tk.yannickfelix.dronespace import *
from tk.yannickfelix.jsonNetCode import *
from tkinter import *
from tkinter import messagebox


class Gamecontroller(object):
    textoutput = None
    textinput = None
    userinput = None
    window = None
    closeFunc = None
    stdCmds = None
    wins = []
    entities = []

    def __init__(self, textoutput, textinput, userinput, window, closeFunc, globalvars):
        """

        @param textoutput: GTextOutput
        @param textinput: GTextInput
        @param userinput: GUserInput
        @param window: GWindow
        @param closeFunc: function
        """
        self.textinput = textinput
        self.textoutput = textoutput
        self.userinput = userinput
        self.window = window
        self.closeFunc = closeFunc
        self.stdCmds = StdCommands(globalvars)

        self.textoutput.printMessage("B.E.N.'s Dronecontroller v2.3b", "left")
        self.textoutput.printMessage("Starting Services...", "left")
        self.textoutput.printMessage("We're searching for files...", "left")
        text = """
                                     ,
              ,-.       _,---._ __  / \\
             /  )    .-'       `./ /   \\
            (  (   ,'            `/    /|
             \  `-"             \\'\   / |
              `.              ,  \ \ /  |
               /`.          ,'-`----Y   |
              (            ;        |   '
              |  ,-.    ,-'         |  /
              |  | (   |    Files?  | /
              )  |  \  `.___________|/
              `--'   `--'
        """
        self.textoutput.printMessage(text, "left", "", False)
        while self.textoutput.writing:
            self.textoutput.writeTick()
            self.window.window.update()
            self.window.window.update_idletasks()
            time.sleep(0.01)
        self.textoutput.printMessage("Ready.", "left")

    def load(self):
        json = Filesystem.loadFile("../../savegame.json")
        i = 0
        for elem in json:
            if json[elem]['class'] == "drone":
                self.entities.append(Drone.fromDict(i, json[elem],self.textoutput.printMessage))
            i+=1

    def update(self):
        self.textoutput.writeTick()
        cmd = self.textinput.getUserText()
        self.textoutput.updateInputting(self.textinput.entry.get())
        self.textoutput.printMessage(cmd, "right", "", True, False)
        self.stdCmds.handleCommand(cmd)

    def openWindow(self,arg=None):
        if len(self.wins) > 1:
            self.wins[randint(1, len(self.wins)-1)].destroy()
        t = Toplevel()
        t.title("Error")
        self.wins.append(t)
        f = Frame(master=t)
        f.place(x=0, y=0, width=200, height=200)
        btn = Button(master=f, text="Error", command=self.openWindow)
        t.bind("<Return>", self.openWindow)
        btn.place(x=50, y=150, width=100, height=20)