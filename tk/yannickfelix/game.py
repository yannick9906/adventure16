"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
import time

from tk.yannickfelix.tkwrapper import *
from tk.yannickfelix.cGamecontroller import *


def close(arg=False):
    globalvars['running'] = False

def toggleFullscreen():
    globalvars['fullscreen'] = not globalvars['fullscreen']

globalvars = {"running":True, "fullscreen":False}
window = GWindow(globalvars)

# story = StoryController(window.textoutput)
# story.loadStory()
# story.update()
gc = Gamecontroller(window.textoutput, window.textinput, window.userinput, window, close, globalvars)
gc.load()
window.window.protocol("WM_DELETE_WINDOW", close)
window.window.bind("<Escape>", close)
window.textinput.entry.bind("<Escape>", close)
window.textinput.entry.bind("<F11>", toggleFullscreen)
while globalvars['running']:
    gc.update()
    window.window.update_idletasks()
    window.window.update()
    window.textinput.entry.focus()
    window.update()
    time.sleep(0.05)
