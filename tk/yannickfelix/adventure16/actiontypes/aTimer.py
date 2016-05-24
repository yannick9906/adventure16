"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
import time
from tk.yannickfelix.adventure16.actiontypes.BasicAction import *


class ATimer(object):
    value = 0
    startTime = 0
    currValue = False
    goto = 0

    def __init__(self, value, goto):
        self.value = value
        self.goto = goto

    def runAction(self):
        print("startTime: {0}; currTime: {1}".format(self.startTime, time.time()))
        if self.startTime == 0:
            self.startTime = time.time()
        else:
            if (self.startTime + self.value) <= time.time():
                self.currValue = True

    def completeAction(self):
        if self.currValue:
            return 1
        else: return -1
