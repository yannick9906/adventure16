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
from tk.yannickfelix.dronespace16.gui.gGameConsole import *
from tk.yannickfelix.dronespace16.gui.gGameInput import *


class GWindow(tk.Tk):
    # Basic Values
    globalvars = None
    isFullscreen = False
    initalsize = ()

    # UI Components
    mainFrame = None
    gameConsole = None
    gameInput = None

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
        super().__init__() # Initialize Tkinter
        # Filling basic values
        self.globalvars = globalvars
        self.isFullscreen = globalvars['fullscreen']
        self.initalsize = size

        #Window initialization
        self.title(title)
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()

        if self.isFullscreen: # If Fullscreen is requested from startup
            self.attributes("-fullscreen", 1) # Removes all window decorations
            self.geometry("{0}x{1}-1-1".format(w, h)) # Set the size of the screen as window size
            super().update_idletasks() # Needed to let the WM make the window
            self.attributes("-topmost", "yes") # Makes the window above everything else
        else:
            startx = int((w * .5) - (size[0] * .5)) # Calculations for centering the window
            starty = int((h * .5) - (size[1] * .5))
            self.geometry("{0}x{1}+{2}+{3}".format(size[0], size[1], startx, starty)) # Set the size of the window
            super().update_idletasks()
        super().update()

        # Creating UI Components
        self.mainFrame = ttk.Frame(master=self, borderwidth=0)
        self.gameConsole = GGameConsole(self, globalvars)
        self.gameInput = GGameInput(self)

        # Adding UI Components to window
        self.mainFrame.pack(fill=tk.BOTH, expand=1)
        self.gameConsole.place(x=0, y=0, height=h, width=w)
        self.gameInput.place(x=-30, y=-30, height=0, width=0)

        #Finally update the window with all new components
        super().update()
        super().update_idletasks()

    def update(self):
        """
            This method should be called once per frame.
            It updates the window.
        """
        # Current size of the Mainframe aka innerWindow
        currentHeight = self.mainFrame.winfo_height()
        currentWidth  = self.mainFrame.winfo_width()
        self.gameConsole.place(x=0, y=0, height=currentHeight, width=currentWidth)
        # Checks if the fullscreenvalue in globalvars has changed
        if self.isFullscreen != self.globalvars['fullscreen']:
            # And changes the fullscreen state
            self.toggleFullscreen()
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
            # We're currently in fullscreen, but Windowed is requested
            # TODO Write something

            time.sleep(1) # For the special effect :)
            self.attributes("-fullscreen", 0) # Turn off fullscreen

            # Set the window into its inital size
            startx = int((w * .5) - (self.initalsize[0] * .5))  # Calculations for centering the window
            starty = int((h * .5) - (self.initalsize[1] * .5))
            self.geometry("{0}x{1}+{2}+{3}".format(self.initalsize[0], self.initalsize[1], startx, starty)) # Set the size of the window
            self.state = "normal" # Should turn of Maximize
            # Once again, update the window
            super().update()
            super().update_idletasks()

            #Todo some nice text
        else:
            # We're currently windowed, so turn on fullscreen
            # TODO write something

            time.sleep(1) # For the special effect :)
            self.attributes("-fullscreen", 1) # Turn on fullscreen and remove all decorations
            self.geometry("{0}x{1}-1-1".format(w, h)) # Set the size of the screen as window size
            super().update_idletasks() # Needed to let the WM update the window
            self.attributes("-topmost", "yes") # Makes the window above everything else
            # Once again, update the window
            super().update()
            super().update_idletasks()

            # Todo some nice text

        self.isFullscreen = not self.isFullscreen # Invert the fullscreenstate
