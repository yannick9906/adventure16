"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
import time

from tk.yannickfelix.dronespace16.gui import *
from yannickfelix.dronespace import Drone
from yannickfelix.jsonNetCode import Filesystem


class GameMasterController(object):

    globalvars = None

    def __init__(self):
        """
        Creates nearly every class needed
        """
        # Init globalvars
        self.globalvars = {
            "res_folder": "../../../res/",
            "running": True,
            "fullscreen": False,
            "class_gui": None,
            "class_gconsole": None,
            "class_ginput": None
        }

        # Init UI and save the references to globalvars
        self.globalvars['class_gui'] = GWindow(self.globalvars)
        self.globalvars['class_gconsole'] = self.globalvars['class_gui'].gameConsole
        self.globalvars['class_ginput'] = self.globalvars['class_gui'].gameInput

        # Welcome / Startup messages -> TODO Auslagern
        self.globalvars['class_gconsole'].printMessage("B.E.N.'s Dronecontroller v2.3b", "left")
        self.globalvars['class_gconsole'].printMessage("Starting Services...", "left")
        self.globalvars['class_gconsole'].printMessage("We're searching for files...", "left")
        text = """
                                         ,
                  ,-.       _,---._ __  / \\
                 /  )    .-'       `./ /   \\
                (  (   ,'            `/    /|
                 \  `-"             \\'\   / |
                  `.              ,  \ \ /  |
                   /`.          ,'-`----Y   |
                  (            ;        |   '
                  |  ,-.    ,-'         |  /
                  |  | (   |    Files?  | /
                  )  |  \  `.___________|/
                  `--'   `--'
            """
        self.globalvars['class_gconsole'].printMessage(text, "left", "", False)
        self.globalvars['class_gconsole'].printMessage("Ready.", "left")
        self.globalvars['class_gconsole'].waitAndWrite()

        while self.globalvars['running']: self.update()

    def load(self):
        pass
        """json = Filesystem.loadFile("../../savegame.json")
        i = 0
        for elem in json:
            if json[elem]['class'] == "drone":
                self.entities.append(Drone.fromDict(i, json[elem], self.textoutput.printMessage))
            i += 1"""

    def update(self):
        self.globalvars['class_gconsole'].writeTick()
        cmd = self.globalvars['class_ginput'].getUserText()
        self.globalvars['class_gconsole'].updateInputting(self.globalvars['class_ginput'].get())
        self.globalvars['class_gconsole'].printMessage(cmd, "right", "", True, False)
        self.globalvars['class_gconsole'].printMessage(cmd, "left", "", True, True)
        self.globalvars['class_gui'].update()
        self.globalvars['class_ginput'].focus()
        time.sleep(0.02)


mc = GameMasterController()