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
window = GWindow()

# story = StoryController(window.textoutput)
# story.loadStory()
# story.update()
gc = Gamecontroller(window.textoutput, window.textinput, window.userinput)
gc.load()
while True:
    window.window.update_idletasks()
    window.window.update()
    # story.update()
    gc.update()
    time.sleep(0.02)
