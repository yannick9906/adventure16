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
import tkinter.ttk as ttk
import time
from tk.yannickfelix.dronespace16.gui import *
from tkinter import messagebox

class GWindow(tk.Tk):
    # Basic Values
    globalvars = None
    isFullscreen = False
    initalsize = ()
    timesincelastframe = 0
    lastFrame = time.time()
    frameCount = 0
    frameCountStart = 0
    lastFrameCount = 0

    # UI Components
    mainFrame = None
    gameConsole = None
    gameInput = None
    upsLabel = None

    def __init__(self, globalvars, title="Dronespace", size=(1024, 576)):
        """
        Creates the window with given settings

        @param globalvars: The epic globalvars dict
        @param title: The windows title
        @param size: the size of the window: (w, h)

        @type globalvars: dict
        @type title: str
        @type size: tuple
        """
        super().__init__()  # Initialize Tkinter
        # Filling basic values
        self.globalvars = globalvars
        self.isFullscreen = globalvars['fullscreen']
        self.initalsize = size

        # Window initialization
        self.title(title)
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()

        if self.isFullscreen:  # If Fullscreen is requested from startup
            self.attributes("-fullscreen", 1)  # Removes all window decorations
            self.geometry("{0}x{1}-1-1".format(w, h))  # Set the size of the screen as window size
            super().update_idletasks()  # Needed to let the WM make the window
            self.attributes("-topmost", "yes")  # Makes the window above everything else
        else:
            startx = int((w * .5) - (size[0] * .5))  # Calculations for centering the window
            starty = int((h * .5) - (size[1] * .5))
            self.geometry("{0}x{1}+{2}+{3}".format(size[0], size[1], startx, starty))  # Set the size of the window
            super().update_idletasks()
        super().update()

        # Creating UI Components
        self.mainFrame = ttk.Frame(master=self, borderwidth=0)
        self.gameConsole = GGameConsole(self.mainFrame, globalvars)
        self.gameInput = GGameInput(self.mainFrame)
        self.upsLabel = tk.Text(master=self.mainFrame, background="black", font=("ProggySquareTTSZ", 12), fg="red",
                                borderwidth=0)
        # Adding UI Components to window
        self.mainFrame.pack(fill=tk.BOTH, expand=1)
        self.gameConsole.place(x=0, y=0, height=h, width=w)
        self.gameInput.place(x=-30, y=-30, height=0, width=0)
        # self.upsLabel.place(x=2, y=2, height=35, width=150)

        # Add Keylisteners
        self.gameInput.bind("<Escape>", self.onESC)
        self.gameInput.bind("<F11>", self.onF11)
        self.protocol("WM_DELETE_WINDOW", self.onESC)

        # Finally update the window with all new components
        super().update()
        super().update_idletasks()

    def update(self):
        """
            This method should be called once per frame.
            It updates the window.
        """
        # Current size of the Mainframe aka innerWindow
        currentHeight = self.mainFrame.winfo_height()
        currentWidth = self.mainFrame.winfo_width()
        self.gameConsole.place(x=0, y=0, height=currentHeight, width=currentWidth)
        # Checks if the fullscreenvalue in globalvars has changed
        if self.isFullscreen != self.globalvars['fullscreen']:
            # And changes the fullscreen state
            self.toggleFullscreen()

        # UPS Calculations
        self.timesincelastframe = time.time() - self.lastFrame
        self.globalvars['frametime'] = self.timesincelastframe
        self.lastFrame = time.time()
        self.upsLabel.delete("1.0", tk.END)

        # Some easier method for the ups
        if self.frameCountStart + 1 <= time.time():
            self.lastFrameCount = self.frameCount
            self.frameCount = 0
            self.frameCountStart = time.time()
        self.frameCount += 1

        try:
            ups = 1 / self.timesincelastframe
            self.globalvars['fps'] = ups
            self.upsLabel.insert(tk.END, "UPS: {:10.2f}U/s\nFrametime: {:.2f}ms\nFPS: {:10.0f}".format(ups, (
            self.timesincelastframe * 1000), self.lastFrameCount))
        except ZeroDivisionError:
            ups = self.lastFrameCount

            self.upsLabel.insert(tk.END, "UPS: {0}U/s\nFrametime: {1}ms".format(ups, (self.timesincelastframe * 1000)))

        # Finally update the window, as usual
        super().update_idletasks()
        super().update()

    def toggleFullscreen(self):
        """
        This method toggles the fullscreenstate.
        DO NOT call this method from outside, instead
        set globalvars['fullscreen'] to True or False
        """
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        if self.isFullscreen:
            self.isFullscreen = not self.isFullscreen  # Invert the fullscreenstate
            # We're currently in fullscreen, but Windowed is requested
            self.gameConsole.printMessage("Leaving fullscreen mode...", "left", "Magic Windowmanager", True, True)
            self.gameConsole.waitAndWrite()
            time.sleep(1)  # For the special effect :)
            self.attributes("-fullscreen", 0)  # Turn off fullscreen

            # Set the window into its inital size
            startx = int((w * .5) - (self.initalsize[0] * .5))  # Calculations for centering the window
            starty = int((h * .5) - (self.initalsize[1] * .5))
            self.geometry("{0}x{1}+{2}+{3}".format(self.initalsize[0], self.initalsize[1], startx,
                                                   starty))  # Set the size of the window
            self.state = "normal"  # Should turn of Maximize
            # Once again, update the window
            super().update()
            super().update_idletasks()

            self.gameConsole.printMessage("It is so small in here... HELP!", "center")
        else:
            # We're currently windowed, so turn on fullscreen
            self.isFullscreen = not self.isFullscreen  # Invert the fullscreenstate
            self.gameConsole.printMessage("Entering fullscreen mode...", "left", "Magic Windowmanager", True, True)
            self.gameConsole.waitAndWrite()

            time.sleep(1)  # For the special effect :)
            self.attributes("-fullscreen", 1)  # Turn on fullscreen and remove all decorations
            self.geometry("{0}x{1}-1-1".format(w, h))  # Set the size of the screen as window size
            super().update_idletasks()  # Needed to let the WM update the window
            self.attributes("-topmost", "yes")  # Makes the window above everything else
            # Once again, update the window
            super().update()
            super().update_idletasks()

            self.gameConsole.printMessage("Ahh, finally some more pixels around me.", "center")

    def onF11(self, arg=True):
        """
        Callback for F11-press -> fullscreentoggle
        @param arg: Event
        """
        self.globalvars['fullscreen'] = not self.globalvars['fullscreen']

    def onESC(self, arg=True):
        """
        Callback for ESC-press or X-click -> stop game
        @param arg: Event
        """
        if messagebox.askyesno("Close", "Do you really want to quit?"):
            self.globalvars['running'] = False
