"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
import tkinter.ttk as ttk


class GGameInput(ttk.Entry):
    lastString = ""

    def __init__(self, master):
        """
         Creates a new TextInput Entry and handler
         @param master: The master of this entry
         @type master: GWindow
        """
        super().__init__(master)
        self.bind("<Return>", self.onEnterUp)

    def hasUserTypedSomething(self):
        """
         @return: If the user has typed something, that hasn't gotten yet
         @rtype: bool
        """
        return self.lastString != ""

    def getUserText(self):
        """
         Returns the last string entered by the user, and confirmed with enter
         @return: see above
         @rtype: str
        """
        string = self.lastString
        self.lastString = ""
        return string

    def onEnterUp(self, arg=False):
        """
         Callback for Enterkey press
        """
        self.lastString = self.get()
        self.clearUserText()

    def clearUserText(self):
        """
         Deletes everything from this text entry
        """
        self.delete(0, 'end')
