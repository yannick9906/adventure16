# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""

from tk.yannickfelix.dronespace16.actions.cActionHandler import *


class DroneActionHandler(ActionHandler):
    dronevars = {}

    def __init__(self, globalvars, dronevars):
        """
        This class handles action

        @param globalvars: The typical globalvars dict
        @type globalvars: dict
        """
        super().__init__(globalvars)
        self.dronevars = dronevars

    def handleAction(self, action, args):
        """
         This magic method decides which function should be called
         @param action: a string with the Action type
         @param args: all the other args

         @type action: str
         @type args: dict
         """
        if action == "listcmd":
            self.ac_listCMD(args)
        elif action == "listinfo":
            self.ac_listInfo(args)
        elif action == "move":
            self.ac_move(args)
        elif action == "listentity":
            self.ac_listEntity(args)
        else:
            super().handleAction(action, args)

    def valueof(self, value, args):
        """
        This method returns the value of a var if it is one
        @param value: String to check
        @type value: str

        @return: The value
        @rtype: str
        """
        if isinstance(value, str):
            if value.startswith("#"):
                return self.dronevars.get(value[1:], False)
            else: return super().valueof(value, args)
        else: return value

    def ac_listCMD(self, args):
        """
        This is a special Drone Action.
        It lists all available commands for this drone.
        @param args: dict
        """
        self.globalvars['class_gconsole'].printMessage("Here's what you can do with me:", "left", self.dronevars['class'].name)
        print("listing Cmds")

        for cmd in self.dronevars['class'].getCmds():
            print(cmd)
            self.globalvars['class_gconsole'].printMessage(cmd, "left", newline=False)

    def ac_listInfo(self, args):
        """
        This is a special Drone Action.
        It prints a detailed information screen of this drone
        @param args: dict
        """
        self.globalvars['class_gconsole'].printMessage(self.dronevars['class'].detailedInfo(), "left", autowrap=False, markup=True)

    def ac_move(self, args):
        """
        This is a special Drone Action.
        It will move the drone to a new entity.
        This one will need one argument to be issued.
        @param args: dict
        """
        try:
            newEntity = self.dronevars['class'].currRoom.getEntity(int(self.valueof(args["entity"], args))-1)
            if newEntity is not None:
                self.dronevars['class'].currEntity = newEntity
                self.globalvars['class_gconsole'].printMessage(
                    "Moving to \"{0}\"".format(newEntity.name), "left")
                self.dronevars['class'].move(1)
            else:
                self.globalvars['class_gconsole'].printMessage(
                    "That doesn't look like a destination to me...", "left")
        except KeyError:
            self.globalvars['class_gconsole'].printMessage("You should at least provide me a destination, since I hasn't been programmed to dance", "left")

    def ac_listEntity(self, args):
        room = self.dronevars['class'].currRoom
        entities = room.getEntities()

        self.globalvars['class_gconsole'].printMessage("This drone is in Room \"__{0}__\".".format(room.name), "left", newline=False, markup=True)
        for i, entity in enumerate(entities):
            if self.dronevars['class'].currEntity == entity:
                self.globalvars['class_gconsole'].printMessage("**{0}: {1} <**".format(i+1, entity.name), "left", newline=False, markup=True)
            else:
                self.globalvars['class_gconsole'].printMessage("{0}: {1}".format(i+1, entity.name), "left", newline=False)
        self.globalvars['class_gconsole'].printMessage("Use \"__drone mv <id>__\" to move to one entity.", "left", newline=False, markup=True)