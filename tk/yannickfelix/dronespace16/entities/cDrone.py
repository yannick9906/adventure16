"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""


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

    currHealth = 0
    currCargoSize = 0
    currEnergyLevel = 0

    def __init__(self, globalvars, name, maxhealth, damage, maxcargosize, maxenergy, baseweight, baseenergydraw):
        """
        @param globalvars: The usual globalvars
        @param name: The drones name
        @param maxhealth: The maximum health value in HP
        @param damage: The damage this class does to enemies with one hit
        @param maxcargosize: The maximum cargo size in Liter
        @param maxenergy: The maxium energy stored in EU
        @param baseweight: The base weight of the drone w/o cargo

        @param globalvars: dict
        @param droneid: int
        @param name: str
        @param maxhealth: int
        @param damage: float
        @param maxcargosize: int
        @param maxenergy: int
        @param baseweight: float
        """
        self.name = name
        self.maxHealth = maxhealth
        self.damage = damage
        self.maxCargosize = maxcargosize
        self.maxEnergy = maxenergy
        self.baseWeight = baseweight
        self.globalvars = globalvars
        self.baseEnergyDraw = baseenergydraw

    def resetVars(self):
        """
        Resets the field of this class.
        """
        self.currHealth = self.maxHealth
        self.currEnergyLevel = self.maxEnergy
        self.currCargoSize = self.baseWeight

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
        self.currEnergyLevel -= self.baseEnergyDraw * (1/self.globalvars['frametime'])
        if self.currEnergyLevel <= 0:
            self.globalvars['cb_noenergy'](self.droneID)
