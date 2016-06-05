# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from . import *


class EntitiesFactory(object):
    globalvars = {}

    def __init__(self, globalvars):
        self.globalvars = globalvars

    def get(self, ID, dict):
        type = dict['type']
        if type == "drone":
            return DroneFactory(self.globalvars).getDrone(ID, dict)

    def getList(self, dict):
        list = []
        for key, elem in enumerate(dict):
            list.append(self.get(key, elem))
        return list
