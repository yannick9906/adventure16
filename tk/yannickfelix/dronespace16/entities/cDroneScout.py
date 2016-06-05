# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.dronespace16.entities.cDrone import *


class DroneScout(Drone):

    def __init__(self, globalvars, name, maxhealth, damage, maxcargosize, maxenergy, baseweight, baseenergydraw):
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
        super().__init__(globalvars, name, maxhealth, damage, maxcargosize, maxenergy, baseweight, baseenergydraw)

