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
from ctypes import windll, byref, create_unicode_buffer, create_string_buffer

import time


class GTextOutput(object):
    text = ""
    showing = 7
    viewx = 36
    viewymax = 45
    fontsize = 18
    #font = "JoystixMonospace-Regular"
    font = "ProggySquareTTSZ"

    label = None
    lastname = ""
    writing = False

    def __init__(self, master):
        """
        @rtype: GTextOutput
        @param master: object
        """
        self.loadfont("../../font4.ttf")
        self.label = tk.Text(master=master, font=(self.font, self.fontsize), background="black", fg="#18F500", borderwidth=0)
        self.label.tag_configure("TEST", font=(self.font, self.fontsize, "bold"))

    def printMessage(self, text, side, name="",autowrap=True, writing=True):
        """
        Prints the requested message onto the Label
        @param text: str
        @param side: str
        @param name: str
        """
        self.viewx = int(self.label.master.winfo_width() / 11.1)
        if text != "":
            self.removeLastLine()
            nameLength = len(name+"> ")
            if autowrap: lines = textwrap.wrap(text, self.viewx-nameLength-(nameLength*0.1))
            else: lines = text.split("\n")
            if side == "left":
                self.text += name+"> " + lines[0] + "\n"
                lines.pop(0)
                if autowrap: lines = textwrap.wrap(" ".join(lines), self.viewx)
                else: lines = text.split("\n")[1:]
                for line in lines:
                    self.text += line + "\n"
            elif side == "right":
                self.text += (" "*(self.viewx-nameLength-len(lines[0]))) + lines[0] + " <"+ name + "\n"
                lines.pop(0)
                if autowrap: lines = textwrap.wrap(" ".join(lines), self.viewx)
                else: lines = text.split("\n")[1:]
                for line in lines:
                    lineLength = len(line)
                    self.text += (" "*(self.viewx-lineLength)) + line + "\n"

            elif side == "center":
                lines = textwrap.wrap(text, self.viewx)
                for line in lines:
                    lineLength = len(line)
                    self.text += (" " * ((self.viewx - lineLength)//2)) + line + "\n"
            self.text += "\n"
            text = str.split(self.text, "\n")
            self.text = "\n".join(text[-self.viewymax:])
            if writing:
                self.writing = True
                lastname = name
            else:
                self.label.insert(tk.END, self.text)
                if side == "left": self.highlight_pattern(name+">", "TEST")
                elif side == "right": self.highlight_pattern("<"+name, "TEST")
                self.writing = False
                self.text = ""
            self.label.see(tk.END)

    def updateInputting(self, currInput):
        if not self.writing:
            self.removeLastLine()
            caret = " "
            if time.time() % 0.5 <= 0.25: caret = "_"
            lineLength = len(currInput+" <")+1
            self.label.insert(tk.END, " "*(self.viewx-lineLength)+currInput+caret+" <")
            self.label.see(tk.END)

    def writeTick(self):
        if self.text != "":
            char = self.text[:4]
            self.label.insert(tk.END, char)
            self.text = self.text[4:]
        else:
            self.writing = False
            self.highlight_pattern(self.lastname + ">", "TEST")
            self.highlight_pattern(">"+self.lastname, "TEST")
        self.label.see(tk.END)
        self.viewx = int(self.label.winfo_width()/11.1)

    def removeLastLine(self):
        self.label.delete('end -1 lines', 'end -1 lines lineend')
        """textarr = self.text.split("\n")
        textarr.pop()
        self.text = "\n".join(textarr)
        self.text += "\n"""


    def highlight_pattern(self, pattern, tag, start="1.0", end="end", regexp=False):
        """
         the given tag to all text that matches the given pattern

        If 'regexp' is set to True, pattern will be treated as a regular
        expression according to Tcl's regular expression syntax.
        @param pattern: str
        @param tag: str
        @param start: str
        @param end: str
        @param regexp: bool
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

    def loadfont(self, fontpath, private=True, enumerable=False):
        """
        Makes fonts located in file `fontpath` available to the font system.

        See https://msdn.microsoft.com/en-us/library/dd183327(VS.85).aspx
        @param private: if True, other processes cannot see this font, and this font will be unloaded when the process dies
        @type private: bool
        @param enumerable: if True, this font will appear when enumerating fonts
        @type enumerable: bool
        @return:

        """
        # This function was taken from
        # https://github.com/ifwe/digsby/blob/f5fe00244744aa131e07f09348d10563f3d8fa99/digsby/src/gui/native/win/winfonts.py#L15
        # This function is written for Python 2.x. For 3.x, you
        # have to convert the isinstance checks to bytes and str
        FR_PRIVATE = 0x10
        FR_NOT_ENUM = 0x20

        if isinstance(fontpath, bytes):
            pathbuf = create_string_buffer(fontpath)
            AddFontResourceEx = windll.gdi32.AddFontResourceExA
        elif isinstance(fontpath, str):
            pathbuf = create_unicode_buffer(fontpath)
            AddFontResourceEx = windll.gdi32.AddFontResourceExW
        else:
            raise TypeError('fontpath must be of type str or unicode')

        flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
        numFontsAdded = AddFontResourceEx(byref(pathbuf), flags, 0)
        return bool(numFontsAdded)