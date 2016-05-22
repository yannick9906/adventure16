"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""

from tk.yannickfelix.tkwrapper.gWindow import *
from tk.yannickfelix.jsonNetCode.cFilesystem import *
from tk.yannickfelix.adventure16.cStoryController import *

window = GWindow()

window.textoutput.printMessage("Das ist ein Test", "left", "Tester")
window.textoutput.printMessage("So so, dass glaubst auch nur du", "right", "Tester2")
window.textoutput.printMessage("Tester2 wurde gemuted gemuted gemuted gemuted gemuted gemuted", "center")
window.userinput.activateAnsButtons(10)
story = StoryController()
story.loadStory()
print(Filesystem.loadFile("../../storyPrimitive.json"))
window.window.mainloop()

