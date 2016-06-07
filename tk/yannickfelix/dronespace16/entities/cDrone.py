# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.dronespace16.entities import *
from tk.yannickfelix.dronespace16.entities.cDroneActionController import *
from tk.yannickfelix.dronespace16.cmds import *


class Drone(object):
    globalvars = {}
    droneID = 0
    name = ""
    maxHealth = 0
    damage = 0
    maxCargosize = 0
    maxEnergy = 0
    baseWeight = 0
    baseEnergyDraw = 0
    commands = {}

    currHealth = 0
    currCargoSize = 0
    currEnergyLevel = 0

    actionhandler = None
    dronevars = {"name":"", "type":"", "currHealth":"", "currEnergy":"", "currCargo":"", "maxEnergy":"", "maxHealth":"", "maxCargo":"", "class":"", "baseEnergyDraw":"", "baseWeight":"", "damage":""}

    def __init__(self, globalvars, name, maxhealth, damage, maxcargosize, maxenergy, baseweight, baseenergydraw, commands):
        """
        @param globalvars: The usual globalvars
        @param name: The drones name
        @param maxhealth: The maximum health value in HP
        @param damage: The damage this class does to enemies with one hit
        @param maxcargosize: The maximum cargo size in Liter
        @param maxenergy: The maxium energy stored in EU
        @param baseweight: The base weight of the drone w/o cargo
        @param commands: The commands this drone can do

        @type globalvars: dict
        @type droneid: int
        @type name: str
        @type maxhealth: int
        @type damage: float
        @type maxcargosize: int
        @type maxenergy: int
        @type baseweight: float
        @type commands: dict
        """
        self.name = name
        self.maxHealth = maxhealth
        self.damage = damage
        self.maxCargosize = maxcargosize
        self.maxEnergy = maxenergy
        self.baseWeight = baseweight
        self.globalvars = globalvars
        self.baseEnergyDraw = baseenergydraw
        self.commands = CommandFactory().listOCommands(commands)
        self.makedronevars()
        self.actionhandler = DroneActionController(globalvars, self.dronevars)

    def resetVars(self):
        """
        Resets the field of this class.
        """
        self.currHealth = self.maxHealth
        self.currEnergyLevel = self.maxEnergy
        self.currCargoSize = self.baseWeight

    def makedronevars(self):
        self.dronevars["type"] = "none"
        self.dronevars["name"] = self.name
        self.dronevars["maxEnergy"] = self.maxEnergy
        self.dronevars["maxCargo"] = self.maxCargosize
        self.dronevars["maxHealth"] = self.maxHealth
        self.dronevars["currEnergy"] = self.currEnergyLevel
        self.dronevars["currCargo"] = self.currCargoSize
        self.dronevars["currHealth"] = self.currHealth
        self.dronevars["damage"] = self.damage
        self.dronevars["baseEnergyDraw"] = self.baseEnergyDraw
        self.dronevars["baseWeight"] = self.baseWeight
        self.dronevars["class"] = self

    def getCmds(self):
        list = []
        for command in self.commands:
            list.append(command.command)
        list.sort()
        return list

    def takeDamage(self, amount):
        """

        @param amount: The Amount of Damage
        @type amount: float
        """
        self.currHealth -= amount
        if not self.currHealth <= 0:
            self.globalvars['cb_damaged'](self.droneID, amount, self.maxHealth)
        else:
            self.currHealth = 0
            self.takeDeed(amount)

    def takeDeed(self, amount):
        """
        Will be called when the drone dies
        @param amount: The Amount of Damage resulted in deed
        @type amount: float
        """
        self.globalvars['cb_destroyed'](self.droneID, amount, self.maxHealth)

    def update(self):
        """
        Should be called once per frame. Updates necessary things...
        """
        self.currEnergyLevel -= self.baseEnergyDraw / self.globalvars['fps']
        if self.currEnergyLevel <= 0:
            self.globalvars['cb_noenergy'](self.droneID)

        self.makedronevars()

    def getInfo(self):
        return "{0}: {1} ({2} EU; {3}l)".format(self.droneID, self.name, int(self.currEnergyLevel+.5), self.currCargoSize)

    def detailedInfo(self):
        return "Name:  #\"{0}\"\n" \
               "Typ:     None\n" \
               "Energie: {1:6.1f}/{2:6.1f}EU ({3:.2f}EU/s)\n" \
               "Cargo:   {4:6.1f}/{5:6.1f}l  ({6:6.1f}kg + {7:6.1f}kg)\n" \
               "Health:  {8:6.1f}/{9:6.1f}HP (Damage: {10:02.1f})".format(self.name, self.currEnergyLevel, self.maxEnergy, self.baseEnergyDraw, self.currCargoSize, self.maxCargosize, self.baseWeight, 0, self.currHealth, self.maxHealth, self.damage)

    def handleCMD(self, cmd: str):
        cmd = cmd.replace("drone ", "")
        print("Command:" + cmd)
        for command in self.commands:
            if command.isThisCommand(cmd):
                command.runCommand(self.actionhandler)
                return True
        return False

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def setCurrEnergyLevel(self, energy):
        self.currEnergyLevel = energy

    def getCurrEnergyLevel(self):
        return self.currEnergyLevel

    def setCurrHealth(self, health):
        self.currHealth = health

    def getCurrHealth(self):
        return self.currHealth

    def setID(self, id):
        self.droneID = id

    def getID(self):
        return self.droneID