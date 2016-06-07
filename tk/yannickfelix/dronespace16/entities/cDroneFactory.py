# coding=utf-8
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
from yannickfelix.jsonNetCode import Filesystem


class DroneFactory(object):
    globalvars = {}
    droneTypes = {}

    def __init__(self, globalvars):
        """
        @type globalvars: dict
        """
        self.globalvars = globalvars
        self.droneTypes = Filesystem.loadFile(globalvars['res_folder'] + "entities/drones.json")

    def getDrone(self, id, dict):
        """
        Creates a 'new' drone from savegame
        @param id: Drones id
        @param dict: Drones data

        @type id: int
        @type dict: dict

        @return: Drone
        @rtype: Drone
        """
        if dict['dronetype'] == "transport":
            drone = self.getNewDrone(self.droneTypes['0'])
            drone.setCurrEnergyLevel(dict['currEnergyLevel'])
            drone.setCurrHealth(dict['currHealth'])
            drone.setID(id)
            drone.setName(dict['name'])
            return drone
        elif dict['dronetype'] == "scout":
            drone = self.getNewDrone(self.droneTypes['3'])
            drone.setCurrEnergyLevel(dict['currEnergyLevel'])
            drone.setCurrHealth(dict['currHealth'])
            drone.setID(id)
            drone.setName(dict['name'])
            return drone

    def getNewDrone(self, dict):
        """
        Creates a new emtpy drone from preset
        @param dict: preset
        @type dict: dict

        @return: Drone
        @rtype: Drone
        """
        if dict['name'] == "transport":
            return DroneTransport(self.globalvars, dict["name"], dict["health"], dict["damage"], dict["cargosize"], dict["maxenergy"], dict["baseweight"], dict["baseenergydraw"], dict["cmds"])
        elif dict['name'] == "scout":
            return DroneScout(self.globalvars, dict["name"], dict["health"], dict["damage"], dict["cargosize"], dict["maxenergy"], dict["baseweight"], dict["baseenergydraw"], dict["cmds"])