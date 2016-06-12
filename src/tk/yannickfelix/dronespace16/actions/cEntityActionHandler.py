# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from . import ActionHandler


class EntityActionHandler(ActionHandler):
    entity = None

    def __init__(self, globalvars, entity):
        """
        This class handles action

        @param globalvars: The typical globalvars dict
        @type globalvars: dict
        """
        super().__init__(globalvars)
        self.entity = entity

    def handleAction(self, action, args):
        """
         This magic method decides which function should be called
         @param action: a string with the Action type
         @param args: all the other args

         @type action: str
         @type args: dict
         """
        print(action )
        if action == "listcmd":
            self.ac_listCMD(args)
        elif action == "listinfo":
            self.ac_listInfo(args)
        elif action == "chargedrone":
            self.ac_chargeDrone(args)
        else:
            super().handleAction(action, args)

    def ac_listCMD(self, args):
        """
        This is a special Entity Action.
        It lists all available commands for this entity.
        @param args: dict
        """
        self.globalvars['class_gconsole'].printMessage("Here's what you can do with me:", "left",
                                                       self.entity.name)
        print("listing Cmds")

        for cmd in self.entity.getCmds():
            print(cmd)
            self.globalvars['class_gconsole'].printMessage(cmd, "left", newline=False)

    def ac_listInfo(self, args):
        """
        This is a special Entity Action.
        It prints a detailed information screen of this entity
        @param args: dict
        """
        self.globalvars['class_gconsole'].printMessage(self.entity.detailedInfo(), "left", autowrap=False,
                                                       markup=True)

    def ac_chargeDrone(self, args):
        """
        This is a special Entity Action.
        It charges a drone at given speed
        @param args: dict
        """
        drone = self.globalvars["class_entity"].entities[self.globalvars['class_entity'].selDrone]
        drone.startEnergyConsumption(args['rate'], 10000)
