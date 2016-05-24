"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.adventure16.actiontypes.aTimer import *


class BasicAction(object):
    value = 0

    def __init__(self, value):
        self.value = value

    @staticmethod
    def fromDict(dict):
        if dict['type'] == "timer":
            return ATimer(dict['value'], dict['goto'])

