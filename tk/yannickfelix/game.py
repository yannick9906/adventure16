"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
import time

from tk.yannickfelix.tkwrapper.gWindow import *
from tk.yannickfelix.jsonNetCode.cFilesystem import *
from tk.yannickfelix.adventure16.cStoryController import *

window = GWindow()

story = StoryController(window.textoutput)
story.loadStory()
story.update()

while True:
    window.window.update_idletasks()
    window.window.update()
    story.update()
    time.sleep(0.02)
