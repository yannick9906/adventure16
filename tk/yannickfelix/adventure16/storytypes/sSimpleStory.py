"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.adventure16.actiontypes.BasicAction import *


class SimpleStory(object):
    text = ""
    speaker = ""
    speakertype = ""
    run = False
    action = None

    def __init__(self, text, speaker, speakertype, action):
        self.text = text
        self.speaker = speaker
        self.speakertype = speakertype
        print(action)
        self.action = BasicAction.fromDict(action)

    def runAction(self):
        return self.action.runAction()

    @staticmethod
    def fromDict(dict):
        return SimpleStory(dict['text'], dict['speaker'], dict['speakertype'], dict['action'])

    def runStory(self, textOutput):
        """
        @param textOutput: GTextOutput
        """
        if not self.run:
            textOutput.printMessage(self.text, self.speakertype, self.speaker)
            self.run = True

    def canRun(self):
        return not self.run
