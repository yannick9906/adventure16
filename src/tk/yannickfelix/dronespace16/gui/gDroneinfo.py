# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
import tkinter as tk
from tkinter.font import Font


class GDroneinfo(tk.Text):
    currDrone = None

    w, h = 370, 110
    fontFamily = "Banana Square"
    fontSize = 22

    def __init__(self, master):
        super().__init__(master, font=(self.fontFamily, self.fontSize), fg="red", bg="black", borderwidth=0)

    def update(self):
        if self.currDrone is not None:
            self.delete('1.0', tk.END)
            self.insert(tk.END, self.currDrone.detailedInfo().replace("__", "").replace("**",""))

            w, h = self.master.winfo_width(), self.master.winfo_height()
            self.place(x=w-self.w, y=0, w=self.w, h=self.h)
        else:
            self.pack_forget()
        super().update()

    def setDrone(self, drone):
        """
        @param drone: The current active Drone
        @type drone: Drone
        """
        self.currDrone = drone