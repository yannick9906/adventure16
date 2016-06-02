"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.dronespace16.entities.cDroneTransport import *


class DroneFactory(object):

    def __init__(self):
        pass

    def getDrone(self, dict):
        if dict['name'] == "transport":
            return DroneTransport()