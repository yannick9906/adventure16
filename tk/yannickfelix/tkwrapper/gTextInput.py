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
