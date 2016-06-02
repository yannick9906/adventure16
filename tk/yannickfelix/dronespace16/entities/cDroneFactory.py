"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.dronespace16.entities.cDroneTransport import *
from tk.yannickfelix.dronespace16.entities.cDroneScout import *


class DroneFactory(object):
    globalvars = {}

    def __init__(self, globalvars):
        self.globalvars = globalvars

    def getDrone(self, dict):
        if dict['name'] == "transport":
            return DroneTransport(self.globalvars, dict["name"], dict["health"], dict["damage"], dict["cargosize"], dict["maxenergy"], dict["baseweight"], dict["baseenergydraw"])
        elif dict['name'] == "scout":
            return DroneScout(self.globalvars, dict["name"], dict["health"], dict["damage"], dict["cargosize"], dict["maxenergy"], dict["baseweight"], dict["baseenergydraw"])