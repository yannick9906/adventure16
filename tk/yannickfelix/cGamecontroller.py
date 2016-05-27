"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from random import randint

from tk.yannickfelix.tkwrapper import *
from tk.yannickfelix.dronespace import *
from tk.yannickfelix.jsonNetCode import *
from tkinter import *
from tkinter import messagebox


class Gamecontroller(object):
    textoutput = None
    textinput = None
    userinput = None
    wins = []
    entities = []

    def __init__(self, textoutput, textinput, userinput):
        """

        @param textoutput: GTextOutput
        @param textinput: GTextInput
        @param userinput: GUserInput
        """
        self.textinput = textinput
        self.textoutput = textoutput
        self.userinput = userinput

        self.textoutput.printMessage("B.E.N.'s Dronecontroller v2.3b", "left")
        self.textoutput.printMessage("Starting Services...", "left")
        self.textoutput.printMessage("Ready.", "left")

    def load(self):
        json = Filesystem.loadFile("../../savegame.json")
        i = 0
        for elem in json:
            if json[elem]['class'] == "drone":
                self.entities.append(Drone.fromDict(i, json[elem],self.textoutput.printMessage))
            i+=1

    def update(self):
        cmd = self.textinput.getUserText()
        self.textoutput.updateInputting(self.textinput.entry.get())
        self.textoutput.printMessage(cmd, "right", "")
        if self.entities[0].runCommand(cmd) == -1:
            if cmd == " ":
                self.textoutput.printMessage("Hey, hör auf damit!", "left", "Kitteh")
            elif cmd == " ":
                self.textoutput.printMessage("Naa toll, jetzt hast du's kaputt gemacht", "left", "Kitteh")
            elif cmd == "Hover kitteh":
                self.textoutput.printMessage("Looking for purmision to land", "left", "Hover Kitteh")
            elif cmd == "map()":
                self.textoutput.printMessage("Dis FODMAP is stoopid. I sees no noms at all.", "left", "Space Kitteh")
            elif cmd == "attack()":
                self.textoutput.printMessage("disapproves ur submishinz", "left", "Moderator Kitteh")
            elif cmd == "zombieh kittehs":
                self.textoutput.printMessage("Zombieh Kittehs coming to cuddle you to death", "left", "")
            elif cmd == "destroy.now()":
                self.textoutput.printMessage("Mhh, naja wenn du willst...", "center")
                for i in range(50):
                    self.openWindow()

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