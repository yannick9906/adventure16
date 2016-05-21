"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""

from tk.yannickfelix.tkwrapper.gWindow import *

window = GWindow()

window.textoutput.printMessage("Das ist ein Test", "left", "Tester")
window.textoutput.printMessage("So so, dass glaubst auch nur du", "right", "Tester2")
window.textoutput.printMessage("Tester2 wurde gemuted gemuted gemuted gemuted gemuted gemuted", "center")
window.window.mainloop()

