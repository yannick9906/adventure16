# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.dronespace16.entities.drones.cDrone import *


class DroneTransport(Drone):

    def __init__(self, globalvars, name, maxhealth, damage, maxcargosize, maxenergy, baseweight, baseenergydraw, commands):
        """
        @param name: The drones name
        @param maxhealth: The maximum health value in HP
        @param damage: The damage this class does to enemies with one hit
        @param maxcargosize: The maximum cargo size in Liter
        @param maxenergy: The maxium energy stored in EU
        @param baseweight: The base weight of the drone w/o cargo

        @param name: str
        @param maxhealth: int
        @param damage: float
        @param maxcargosize: int
        @param maxenergy: int
        @param baseweight: float
        """
        super().__init__(globalvars, name, maxhealth, damage, maxcargosize, maxenergy, baseweight, baseenergydraw, commands )


    def detailedInfo(self):
        """
        @return: Long info string
        @rtype: str
        """
        return "Name:  \"{0}\"\n" \
               "Typ:     Transport\n" \
               "Energie: {1:6.1f}/{2:6.1f}EU ({3:.2f}EU/s)\n" \
               "Cargo:   {4:6.1f}/{5:6.1f}l  ({6:6.1f}kg + {7:6.1f}kg)\n" \
               "Health:  {8:6.1f}/{9:6.1f}HP (Damage: {10:02.1f})".format(self.name, self.currEnergyLevel, self.maxEnergy,
                                                                          self.baseEnergyDraw, self.currCargoSize,
                                                                          self.maxCargosize, self.baseWeight, 0,
                                                                          self.currHealth, self.maxHealth, self.damage)
