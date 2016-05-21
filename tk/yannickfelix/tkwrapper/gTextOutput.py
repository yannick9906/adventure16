import textwrap
import tkinter as tk
import tkinter.ttk as ttk


class GTextOutput(object):
    text = ""
    showing = 7
    viewx = 10
    viewy = 0

    label = None

    def __init__(self, master):
        self.label = ttk.Label(master=master, font=("Courier", 12), text="Test")

    def printMessage(self, text, side, name):
        nameLength = len(name+"> ")
        lines = textwrap.wrap(text, self.viewx-nameLength)
        print(lines)
        #lines = str.split(text, "\n")
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
        self.text += "\n"
        self.label.set(text=self.text)
        print(self.text)
