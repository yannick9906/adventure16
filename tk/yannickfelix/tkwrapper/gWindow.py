"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""

from tk.yannickfelix.tkwrapper.gTextInput import *
from tk.yannickfelix.tkwrapper.gTextOutput import *
from tk.yannickfelix.tkwrapper.gUserInput import *


class GWindow(object):
    textoutput = None
    textinput = None
    userinput = None
    quitButton = None
    window = None
    mainFrame = None
    globalvars = None
    fullscreen = False

    def __init__(self, globalvars, title: str="A Game Window"):
        self.globalvars = globalvars
        self.window = tk.Tk()
        self.window.title(title)
        self.fullscreen = globalvars['fullscreen']

        if globalvars['fullscreen']:
            self.window.attributes("-fullscreen",1)
            w, h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
            self.window.overrideredirect(1)
            self.window.geometry("%dx%d-1-1" % (w+2, h+2))
            self.window.update_idletasks()
            self.window.attributes("-topmost", "yes")
        else:
            self.window.geometry("1024x576")

        self.mainFrame = ttk.Frame(master=self.window, borderwidth=0)
        self.mainFrame.pack(fill=tk.BOTH, expand=1)
        width = 1024
        height = 576
        self.textoutput = GTextOutput(master=self.mainFrame)
        self.textoutput.label.place(x=0,y=0,height=height,width=width)
        globalvars['class_textoutput'] = self.textoutput
        self.textinput = GTextInput(master=self.mainFrame)
        self.textinput.entry.place(x=-10, y=-10, width=0, height=0)
        self.userinput = GUserInput(master=self.mainFrame)
        # self.userinput.position.place(x=402, y=520, width=398, height=80)
        self.window.update()

    def update(self):
        width = self.mainFrame.winfo_width()
        height = self.mainFrame.winfo_height()
        self.textoutput.label.place(x=0, y=0, height=height, width=width)
        if self.fullscreen != self.globalvars['fullscreen']:
            self.toggleFullscreen()

    def toggleFullscreen(self):
        if self.fullscreen:
            self.textoutput.printMessage("fullscreen 0", "right", "")
            self.textoutput.printMessage("Leaving Fullscreen...","left","The magic Windowmanager")
            self.textoutput.printMessage("Extremly small resolution of 1024x576", "left", "The magic Windowmanager")
            while self.textoutput.writing:
                self.textoutput.writeTick()
                self.window.update()
                self.window.update_idletasks()
                time.sleep(0.02)
            time.sleep(1)
            self.window.attributes("-fullscreen", 0)
            self.window.geometry("1024x576")
            self.window.state = "normal"
            self.window.update_idletasks()
            self.window.update()
            self.textoutput.writeTick()
            self.textoutput.printMessage("Uhhgh, it so small in here, look at all that wrong wrapped text up here!","center")
        else:
            w, h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
            self.textoutput.printMessage("fullscreen 1", "right", "")
            self.textoutput.printMessage("Entering fullscreen...","left","The magic Windowmanager")
            self.textoutput.printMessage("Whopping resolution of {0}x{1}".format(w,h), "left", "The magic Windowmanager")
            while self.textoutput.writing:
                self.textoutput.writeTick()
                self.window.update()
                self.window.update_idletasks()
                time.sleep(0.02)
            time.sleep(1)
            self.window.attributes("-fullscreen",1)
            #self.window.overrideredirect(1)
            self.window.geometry("%dx%d-1-1" % (w+2, h+2))
            self.window.update_idletasks()
            self.window.attributes("-topmost", "yes")
            self.window.update()
            self.textoutput.printMessage("Ahh, that's better... Much more space here", "center")
        self.fullscreen = not self.fullscreen



