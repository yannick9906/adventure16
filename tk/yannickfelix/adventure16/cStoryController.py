"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from tk.yannickfelix.jsonNetCode.cFilesystem import *
from tk.yannickfelix.adventure16.storytypes.sSimpleStory import *


class StoryController(object):
    story = []
    currStoryID = 0
    textoutput = None

    def __init__(self, textoutput):
        self.textoutput = textoutput

    def loadStory(self):
        for i, e in enumerate(Filesystem.loadFile("../../storyPrimitive.json")):
            self.story.append(self.parseStory(e))

    @staticmethod
    def parseStory(code):
        if code['type'] == "SimpleStory":
            return SimpleStory.fromDict(code)

    def update(self):
        if self.story[self.currStoryID].canRun():
            self.story[self.currStoryID].runStory(self.textoutput)
        else:
            self.story[self.currStoryID].runAction()
            if self.story[self.currStoryID].action.completeAction() == 1:
                self.currStoryID = self.story[self.currStoryID].action.goto
