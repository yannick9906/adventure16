# coding=utf-8
"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
import json


class Filesystem(object):

    def __init__(self):
        pass

    @staticmethod
    def loadFile(filename):
        """
        Loads the given file and parses JSON
        @param filename: The file to load
        @type filename: str

        @return: A parsed version
        @rtype: dict
        """
        return json.load(open(filename, "r"))
