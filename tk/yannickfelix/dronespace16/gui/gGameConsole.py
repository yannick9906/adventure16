# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""

import textwrap
import tkinter as tk
import tkinter.ttk as ttk
from ctypes import windll, byref, create_unicode_buffer, create_string_buffer
import time


class GGameConsole(tk.Text):
    # Misc values
    text = ""
    lastname = ""
    viewX = 36
    isWriting = False
    writeSpeed = 3
    globalvars = None

    # Fontsettings
    fontSize = 18
    # fontFamily = "JoystixMonospace-Regular"
    # fontFile = "font.ttf"
    fontFamily = "ProggySquareTTSZ"
    fontFile = "font4.ttf"

    def __init__(self, master, globalvars):
        """
        Creates the textfield for outputting text
        @param master: The master for this Class
        @type master: GWindow
        """
        self.globalvars = globalvars
        self.loadfont(globalvars['res_folder'] + "fonts/" + self.fontFile)
        # Create the text field
        super().__init__(master, font=(self.fontFamily, self.fontSize), bg="black", fg="#18F500", borderwidth=0)

        # Create needed tags
        self.tag_configure("BOLD", font=(self.fontFamily, self.fontSize, "bold"))

    def printMessage(self, text, side, name="", autowrap=True, writing=True, newline=True):
        """
        Prepares or prints a message onto the text field

        @param text: The text that should be printed
        @param side: The Alignment of the text <left|center|right>
        @param name: The Name on front of the ">" or "<"
        @param autowrap: False if the text is prewrapped
        @param writing: False if it should be printed directly
        @param newline: False if no newline should be added

        @type text: str
        @type side: str
        @type name: str
        @type autowrap: bool
        @type writing: bool
        @type newline: bool
        """
        # update View Values
        self.viewX = int(self.master.winfo_width() / 11.1)

        if text != "" and text != " ":
            self.removeLastLine()
            nameLength = len(name + "> ")  # calculate the length of the name + ">"

            if autowrap: lines = textwrap.wrap(text, self.viewX - nameLength - (nameLength * 0.1)) # autowrap for the first line
            else: lines = text.split("\n")  # If the text is already wrapped, split it at the newlines

            if side == "left":
                # Add the first line to the text, that needs to be printed
                self.text += name + "> " + lines[0] + "\n"
                lines.pop(0)  # And remove this line from lines

                # Add the lines together and wrap them again
                if autowrap: lines = textwrap.wrap(" ".join(lines), self.viewX)

                # Add the remaining lines to the text, that needs to be printed
                for line in lines:
                    self.text += line + "\n"

            elif side == "right":
                # Add the first line with leading spaces for right alignment
                self.text += (" " * (self.viewX - nameLength - len(lines[0]))) + lines[0] + " <" + name
                lines.pop(0)  # And remove this line from lines

                # Add the lines together and wrap them again
                if autowrap: lines = textwrap.wrap(" ".join(lines), self.viewX)

                # Add the remaining lines to the text, that needs to be printed
                for line in lines:
                    lineLength = len(lines)
                    self.text += (" " * (self.viewX - lineLength)) + line + "\n"

            elif side == "center":
                # Wrap the text if autowrap is enabled
                if autowrap: lines = textwrap.wrap(text, self.viewX)
                else: lines = text.split("\n")

                # Add the lines to text
                for line in lines:
                    lineLength = len(line)
                    self.text += (" " * ((self.viewX - lineLength)//2)) + line + "\n"

            if newline:
                self.text += "\n"  # Add a newline

            if writing:
                # Set isWriting to true, so writing starts
                self.isWriting = True
                self.lastname = name
            else:
                # If it should be displayed directly, do not write it
                # Add the text to the end me
                self.insert(tk.END, self.text)

                # Make the name bold
                if side == "left": self.highlight_pattern(name+">", "BOLD")
                elif side == "right": self.highlight_pattern("<"+name, "BOLD")

                # Turn off writing
                self.isWriting = False
                # Clean text
                self.text = ""

            # Scroll down
            self.see(tk.END)

    def updateInputting(self, currInput):
        """
        @todo Do not call this function from outside!

        This method should be called once per frame.
        It updates the textfield if the user is currently
        typing
        @param currInput: The text the user typed
        @type currInput: str
        """
        if not self.isWriting:
            self.removeLastLine()
            caret = " "
            # Make the caret blink
            if time.time() % .5 <= .25: caret = "_"

            # Calculate the length of the line
            lineLength = len(currInput + " <") + 1
            # Add the line to me
            self.insert(tk.END, " " * (self.viewX-lineLength) + currInput + caret + " <")

            # Scroll down
            self.see(tk.END)

    def writeTick(self):
        """
        This method should be called once per frame.
        It writes the next char into the text field
        and updates necessary field of this class.
        """
        if self.text != "" and self.isWriting == True:
            # Get the last char (or 4 or something else)
            char = self.text[:self.writeSpeed]
            self.insert(tk.END, char)
            # Remove this char from the text
            self.text = self.text[self.writeSpeed:]
        elif self.text == "" and self.isWriting == True:
            # Wrinting is finished
            # Turn of writing
            self.isWriting = False
            # highlight the names
            self.highlight_pattern(self.lastname + ">", "BOLD")
            self.highlight_pattern(">" + self.lastname, "BOLD")
        self.markdown()
        # Scroll down
        self.see(tk.END)
        # update View Values
        self.viewX = int(self.master.winfo_width() / 11.1)

    def waitAndWrite(self):
        """
        This method updates the window and writes remaining text onto the screen.
        It returns when it has finished
        """
        while self.isWriting:
            self.writeTick()
            self.master.update()
            time.sleep(0.01)

    def removeLastLine(self):
        """
        Removes the last line from the text field.
        """
        self.delete('end -1 lines', 'end -1 lines lineend')

    def highlight_pattern(self, pattern, tag, start="1.0", end="end", regexp=False):
        """
        the given tag to all text that matches the given pattern
        If 'regexp' is set to True, pattern will be treated as a regular expression according to Tcl's regular expression syntax.

        @type pattern: str
        @type tag: str
        @type start: str
        @type end: str
        @type regexp: bool
        """

        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count = tk.IntVar()
        while True:
            index = self.search(pattern, "matchEnd", "searchLimit", count=count, regexp=regexp)
            if index == "": break
            if count.get() == 0: break  # degenerate pattern which matches zero-length strings
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")

    def deletePattern(self, pattern, start="1.0", end="end", regexp=False):
        """
        @see highlight_pattern()
        The same, but it deletes this part instead of highlighting it

        @type pattern: str
        @type start: str
        @type end: str
        @type regexp: bool
        """
        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count = tk.IntVar()
        while True:
            index = self.search(pattern, "matchEnd", "searchLimit", count=count, regexp=regexp)
            if index == "": break
            if count.get() == 0: break  # degenerate pattern which matches zero-length strings
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.delete("matchStart", "matchEnd")

    def loadfont(self, fontpath, private=True, enumerable=False):
        """
        Makes fonts located in file `fontpath` available to the font system.

        See https://msdn.microsoft.com/en-us/library/dd183327(VS.85).aspx
        @param private: if True, other processes cannot see this font, and this font will be unloaded when the process dies
        @type private: bool
        @param enumerable: if True, this font will appear when enumerating fonts
        @type enumerable: bool
        @rtype: bool

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

    def markdown(self):
        """
        Should do markdown, but ...
        """
        self.highlight_pattern("\".*?\"", "BOLD", regexp=True)
        # self.deletePattern("**")