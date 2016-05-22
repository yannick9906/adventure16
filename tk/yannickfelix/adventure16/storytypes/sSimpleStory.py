"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""


class SimpleStory(object):
    text = ""
    speaker = ""
    speakertype = ""
    action = None

    def __init__(self, text, speaker, speakertype, action):
        self.text = text
        self.speaker = speaker
        self.speakertype = speakertype

    @staticmethod
    def fromDict(dict):
        return SimpleStory(dict['text'], dict['speaker'], dict['speakertype'], dict['action'])


