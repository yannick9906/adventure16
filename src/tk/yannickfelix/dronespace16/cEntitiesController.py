# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.dronespace16.entities import Door
from tk.yannickfelix.jsonNetCode import Filesystem
from tk.yannickfelix.dronespace16.entities.drones import *
from tk.yannickfelix.dronespace16.entities import *


class EntitiesController(object):
    globalvars = {}
    entities = []
    ships = []
    selDrone = -1

    def __init__(self, globalvars):
        """
        @type globalvars: dict
        """
        self.globalvars = globalvars
        self.load()

    def update(self):
        """
        This method should be called once per frame, and updates all Entities
        """
        for e in self.entities:
            if e is not None:
                e.update()

    def load(self):
        """
        This loads the json savegame and
        creates entities from this savegame
        """
        savegame = Filesystem.loadFile("../../../savegame.json")
        self.entities = EntitiesFactory(self.globalvars).getList(savegame['entities'])

    def get(self, id):
        """
        Get a specific entities by it's id
        @param id: The EntityID
        @type id: int
        @return: The requested entity or None
        @rtype: Entity
        """
        try:
            return self.entities[id]
        except IndexError:
            return None

    def handleCommands(self, cmd):
        """
        This handles and forwards entity specific commands
        @param cmd: The command issued
        @type cmd: str

        @return: success
        @rtype: bool
        """
        # Lists all available drones
        if cmd == "drones":
            for e in self.entities:
                if isinstance(e, Drone):  # Only if the entity is an instance of Drone
                    if self.selDrone == e.getID():  drone = e.getInfo() + " <"
                    else: drone = e.getInfo()
                    self.globalvars['class_gconsole'].printMessage(drone, "left",newline=False)
            self.globalvars['class_gconsole'].printMessage("Type in \"__drone sel <droneid>__\" to select a drone","left",newline=False, markup=True)
            return True
        # Selects a adrone
        elif cmd.startswith("drone sel"):
            cmd = cmd.split(" ")
            try:
                # cmd[2] is the drones id
                if int(cmd[2]) <= len(self.entities):
                    if isinstance(self.entities[int(cmd[2])], Drone):
                        self.selDrone = int(cmd[2])
                        self.globalvars['class_gconsole'].printMessage("Current drone change to <{0}: {1}>".format(self.selDrone, self.entities[self.selDrone].getName()), "left")
                    else: self.globalvars['class_gconsole'].printMessage("This drone does not exist (yet).", "left")
                else: self.globalvars['class_gconsole'].printMessage("This drone does not exist (yet).", "left")
            except IndexError:
                # If no id is given, cmd[2] throws a IndexError
                self.globalvars['class_gconsole'].printMessage("Please provide a DroneID", "left")
            finally:
                return True
        # All Cmd starting with drone will be forwarded to the current drone
        elif cmd.startswith("drone "):
            if self.selDrone != -1:
                drone = self.entities[self.selDrone]
                return drone.handleCMD(cmd)
            self.globalvars['class_gconsole'].printMessage("You need to select a drone via \"__drone sel <droneid>__\"", "left", markup=True)
            return True
        # Interact opens doors
        elif cmd == "interact":
            if self.selDrone != -1:
                drone = self.entities[self.selDrone]
                if isinstance(drone.currEntity, Door):
                    if not drone.currEntity.locked:
                        drone.currRoom = drone.currEntity.to
                        drone.currEntity = 0
                        drone.update()
                        self.globalvars['class_gconsole'].printMessage(
                            "Moved to room \"__{0}__\"".format(drone.currRoom.name), "left", markup=True)
                        return True
                    else:
                        self.globalvars['class_gconsole'].printMessage(
                            "Sorry, but this door is locked", "left", markup=True)
                        return True
            self.globalvars['class_gconsole'].printMessage("You need to select a drone via \"__drone sel <droneid>__\"","left", markup=True)
            return True
        # All cmds starting with interact will be forwarded to an entity (not to drones because it's already handled above)
        elif cmd.startswith("interact "):
            if self.selDrone != -1:
                drone = self.entities[self.selDrone]
                if not isinstance(drone.currEntity, int):
                    return drone.currEntity.handleCMD(cmd)
                self.globalvars['class_gconsole'].printMessage("You need to move w/ this drone via \"__drone mv <to>__\"","left", markup=True)
            self.globalvars['class_gconsole'].printMessage("You need to select a drone via \"__drone sel <droneid>__\"","left", markup=True)
            return True
        return False
