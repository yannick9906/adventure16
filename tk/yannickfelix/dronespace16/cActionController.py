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
            self.ac_print(args)
        elif action == "setVar":
            self.ac_setVar(args)
        elif action == "invVar":
            self.ac_invVar(args)
        elif action == "conditionVar":
            self.ac_condition_Var(args)

    def valueof(self, value):
        if isinstance(value, str):
            if value.startswith("$"):
                return self.globalvars.get(value[1:], False)
            else: return value
        else: return value

    def ac_print(self, args):
        text = args['text']
        arg0 = args['args'][0]
        arg1 = args['args'][1]
        arg2 = args['args'][2]
        arg3 = args['args'][3]
        self.globalvars['class_gconsole'].printMessage(text, arg0, arg1, arg2, arg3)

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