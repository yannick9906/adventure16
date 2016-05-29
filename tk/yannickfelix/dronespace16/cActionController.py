"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""


class ActionController(object):
    globalvars = ""

    def __init__(self, globalvars):
        self.globalvars = globalvars

    def handleAction(self, action, args):
        if action == "print":
            pass
        elif action == "setVar":
            pass
        elif action == "invVar":
            pass
        elif action == "conditionVar":
            pass

    def valueof(self, value):
        if value.startswith("$"):
            return self.globalvars.get(value[1:], False)
        else:
            return value

    def ac_print(self, args):
        self.globalvars['class_guiConsole'].printMessage(args['text'], args['args'][0], args['args'][1], args['args'][2], args['args'][3])

    def ac_setVar(self, args):
        self.globalvars[args['var']] = self.valueof(args['value'])

    def ac_invVar(self, args):
        if isinstance(self.globalvars[args['var']], bool):
            self.globalvars[args['var']] = not self.globalvars[args['var']]

    def ac_condition_Var(self, args):
        result = False
        if args['operation'] == "equal":
            result = self.valueof(args['var1']) == self.valueof(args['var2'])
        elif args['operation'] == "bigger":
            result = self.valueof(args['var1']) > self.valueof(args['var2'])
        elif args['operation'] == "smaller":
            result = self.valueof(args['var1']) < self.valueof(args['var2'])
        elif args['operation'] == "not equal":
            result = self.valueof(args['var1']) != self.valueof(args['var2'])

        if result:
            self.handleAction(args['action_true']['action'], args['action_true'])
        else:
            self.handleAction(args['action_false']['action'], args['action_false'])