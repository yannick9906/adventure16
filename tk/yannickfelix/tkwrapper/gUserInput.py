import tkinter as tk
import tkinter.ttk as ttk


class GUserInput(object):
    position = None
    buttonAnsA = None
    buttonAnsB = None
    buttonAnsC = None
    buttonAnsD = None

    def __init__(self, master):
        self.position = tk.Canvas(master=master, bg="green")
        self.buttonAnsA = ttk.Button(master=self.position, text="Antwort A")
        self.buttonAnsB = ttk.Button(master=self.position, text="Antwort B")
        self.buttonAnsC = ttk.Button(master=self.position, text="Antwort C")
        self.buttonAnsD = ttk.Button(master=self.position, text="Antwort D")

        self.buttonAnsA.place(x=0,y=0, width=199, height=40)
        self.buttonAnsB.place(x=199,y=0, width=199, height=40)
        self.buttonAnsC.place(x=0,y=40, width=199, height=40)
        self.buttonAnsD.place(x=199,y=40, width=199, height=40)

        self.deactiveAnsButtons()

    def activateAnsButtons(self, select):
        if (select << 1) & 1: self.buttonAnsA.config(state='active')
        if (select << 2) & 1: self.buttonAnsB.config(state='active')
        if (select << 3) & 1: self.buttonAnsC.config(state='active')
        if (select << 4) & 1: self.buttonAnsD.config(state='active')

    def deactiveAnsButtons(self):
        self.buttonAnsA.config(state='disabled')
        self.buttonAnsB.config(state='disabled')
        self.buttonAnsC.config(state='disabled')
        self.buttonAnsD.config(state='disabled')
