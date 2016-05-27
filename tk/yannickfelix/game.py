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


def close():
    global running
    running = False


window = GWindow()
running = True

# story = StoryController(window.textoutput)
# story.loadStory()
# story.update()
gc = Gamecontroller(window.textoutput, window.textinput, window.userinput)
gc.load()
window.window.protocol("WM_DELETE_WINDOW", close)
while running:
    gc.update()
    window.window.update_idletasks()
    window.window.update()
    window.textinput.entry.focus()
    time.sleep(0.05)
