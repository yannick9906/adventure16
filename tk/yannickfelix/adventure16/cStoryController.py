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

    def __init__(self):
        pass

    def loadStory(self):
        for i, e in enumerate(Filesystem.loadFile("../../storyPrimitive.json")):
            self.story.append(self.parseStory(e))

    def parseStory(self, code):
        if code['type'] == "SimpleStory":
            return SimpleStory.fromDict(code)