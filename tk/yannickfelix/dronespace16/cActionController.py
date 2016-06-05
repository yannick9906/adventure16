# coding=utf-8
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
        """
        This class handles action
        @param globalvars: The typical globalvars dict
        @type globalvars: dict
        """
        self.globalvars = globalvars

    def handleAction(self, action, args):
        """
        This magic method decides which function should be called
        @param action: a string with the Action type
        @param args: all the other args

        @type action: str
        @type args: dict
        """
        if action == "print":
            self.ac_print(args)
        elif action == "setVar":
            self.ac_setVar(args)
        elif action == "invVar":
            self.ac_invVar(args)
        elif action == "conditionVar":
            self.ac_condition_Var(args)

    def valueof(self, value):
        """
        This method returns the value of a var if it is one
        @param value: String to check
        @type value: str

        @return: The value
        @rtype: str
        """
        if isinstance(value, str):
            if value.startswith("$"):
                return self.globalvars.get(value[1:], False)
            else: return value
        else: return value

    def ac_print(self, args):
        """
        This Action simply prints text
        @param args: The action args dict
        @type args: dict
        """
        text = args['text']
        arg0 = args['args'][0]
        arg1 = args['args'][1]
        arg2 = args['args'][2]
        arg3 = args['args'][3]
        self.globalvars['class_gconsole'].printMessage(text, arg0, arg1, arg2, arg3)

    def ac_setVar(self, args):
        """
        This Action set a var onto a specific value or another vars value
        @param args: The action args dict
        @type args: dict
        """
        self.globalvars[args['var']] = self.valueof(args['value'])

    def ac_invVar(self, args):
        """
        This Action invertes a boolean var
        @param args: The action args dict
        @type args: dict
        """
        if isinstance(self.globalvars[args['var']], bool):
            self.globalvars[args['var']] = not self.globalvars[args['var']]

    def ac_condition_Var(self, args):
        """
        This is a more complex action.
        It checks wether <var1> is <operator> than <var2>.
        var1 and var2 can be a value or a var.
        The operator can either be a char(=,!,<,>) or a text("equal").
        If true it starts action_true,
        else it will start action_false.
        @param args: The action args dict
        @type args: dict
        """
        result = False
        if args['operation'] == "equal" or args['operation'] == "==" or args['operation'] == "=":
            result = self.valueof(args['var1']) == self.valueof(args['var2'])
        elif args['operation'] == "bigger" or args['operation'] == ">":
            result = self.valueof(args['var1']) > self.valueof(args['var2'])
        elif args['operation'] == "smaller" or args['operation'] == "<":
            result = self.valueof(args['var1']) < self.valueof(args['var2'])
        elif args['operation'] == "not equal" or args['operation'] == "!=" or args['operation'] == "!":
            result = self.valueof(args['var1']) != self.valueof(args['var2'])

        if result:
            self.handleAction(args['action_true']['action'], args['action_true'])
        else:
            self.handleAction(args['action_false']['action'], args['action_false'])