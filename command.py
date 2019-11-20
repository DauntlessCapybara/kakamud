"""
Commands

Commands describe the input the account can do to the game.

"""

from evennia import Command as BaseCommand

# from evennia import default_cmds


class Command(BaseCommand):
    """
    Inherit from this if you want to create your own command styles
    from scratch.  Note that Evennia's default commands inherits from
    MuxCommand instead.

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    Each Command implements the following methods, called
    in this order (only func() is actually required):
        - at_pre_cmd(): If this returns anything truthy, execution is aborted.
        - parse(): Should perform any extra parsing needed on self.args
            and store the result on self.
        - func(): Performs the actual work.
        - at_post_cmd(): Extra actions, often things done after
            every command, like prompts.

            """

    pass


# -------------------------------------------------------------
#
# The default commands inherit from
#
#   evennia.commands.default.muxcommand.MuxCommand.
#
# If you want to make sweeping changes to default commands you can
# uncomment this copy of the MuxCommand parent and add
#
#   COMMAND_DEFAULT_CLASS = "commands.command.MuxCommand"
#
# to your settings file. Be warned that the default commands expect
# the functionality implemented in the parse() method, so be
# careful with what you change.
#
# -------------------------------------------------------------

# from evennia.utils import utils
#
#
# class MuxCommand(Command):
#     """
#     This sets up the basis for a MUX command. The idea
#     is that most other Mux-related commands should just
#     inherit from this and don't have to implement much
#     parsing of their own unless they do something particularly
#     advanced.
#
#     Note that the class's __doc__ string (this text) is
#     used by Evennia to create the automatic help entry for
#     the command, so make sure to document consistently here.
#     """
#     def has_perm(self, srcobj):
#         """
#         This is called by the cmdhandler to determine
#         if srcobj is allowed to execute this command.
#         We just show it here for completeness - we
#         are satisfied using the default check in Command.
#         """
#         return super().has_perm(srcobj)
#
#     def at_pre_cmd(self):
#         """
#         This hook is called before self.parse() on all commands
#         """
#         pass
#
#     def at_post_cmd(self):
#         """
#         This hook is called after the command has finished executing
#         (after self.func()).
#         """
#         pass
#
#     def parse(self):
#         """
#         This method is called by the cmdhandler once the command name
#         has been identified. It creates a new set of member variables
#         that can be later accessed from self.func() (see below)
#
#         The following variables are available for our use when entering this
#         method (from the command definition, and assigned on the fly by the
#         cmdhandler):
#            self.key - the name of this command ('look')
#            self.aliases - the aliases of this cmd ('l')
#            self.permissions - permission string for this command
#            self.help_category - overall category of command
#
#            self.caller - the object calling this command
#            self.cmdstring - the actual command name used to call this
#                             (this allows you to know which alias was used,
#                              for example)
#            self.args - the raw input; everything following self.cmdstring.
#            self.cmdset - the cmdset from which this command was picked. Not
#                          often used (useful for commands like 'help' or to
#                          list all available commands etc)
#            self.obj - the object on which this command was defined. It is often
#                          the same as self.caller.
#
#         A MUX command has the following possible syntax:
#
#           name[ with several words][/switch[/switch..]] arg1[,arg2,...] [[=|,] arg[,..]]
#
#         The 'name[ with several words]' part is already dealt with by the
#         cmdhandler at this point, and stored in self.cmdname (we don't use
#         it here). The rest of the command is stored in self.args, which can
#         start with the switch indicator /.
#
#         This parser breaks self.args into its constituents and stores them in the
#         following variables:
#           self.switches = [list of /switches (without the /)]
#           self.raw = This is the raw argument input, including switches
#           self.args = This is re-defined to be everything *except* the switches
#           self.lhs = Everything to the left of = (lhs:'left-hand side'). If
#                      no = is found, this is identical to self.args.
#           self.rhs: Everything to the right of = (rhs:'right-hand side').
#                     If no '=' is found, this is None.
#           self.lhslist - [self.lhs split into a list by comma]
#           self.rhslist - [list of self.rhs split into a list by comma]
#           self.arglist = [list of space-separated args (stripped, including '=' if it exists)]
#
#           All args and list members are stripped of excess whitespace around the
#           strings, but case is preserved.
#         """
#         raw = self.args
#         args = raw.strip()
#
#         # split out switches
#         switches = []
#         if args and len(args) > 1 and args[0] == "/":
#             # we have a switch, or a set of switches. These end with a space.
#             switches = args[1:].split(None, 1)
#             if len(switches) > 1:
#                 switches, args = switches
#                 switches = switches.split('/')
#             else:
#                 args = ""
#                 switches = switches[0].split('/')
#         arglist = [arg.strip() for arg in args.split()]
#
#         # check for arg1, arg2, ... = argA, argB, ... constructs
#         lhs, rhs = args, None
#         lhslist, rhslist = [arg.strip() for arg in args.split(',')], []
#         if args and '=' in args:
#             lhs, rhs = [arg.strip() for arg in args.split('=', 1)]
#             lhslist = [arg.strip() for arg in lhs.split(',')]
#             rhslist = [arg.strip() for arg in rhs.split(',')]
#
#         # save to object properties:
#         self.raw = raw
#         self.switches = switches
#         self.args = args.strip()
#         self.arglist = arglist
#         self.lhs = lhs
#         self.lhslist = lhslist
#         self.rhs = rhs
#         self.rhslist = rhslist
#
#         # if the class has the account_caller property set on itself, we make
#         # sure that self.caller is always the account if possible. We also create
#         # a special property "character" for the puppeted object, if any. This
#         # is convenient for commands defined on the Account only.
#         if hasattr(self, "account_caller") and self.account_caller:
#             if utils.inherits_from(self.caller, "evennia.objects.objects.DefaultObject"):
#                 # caller is an Object/Character
#                 self.character = self.caller
#                 self.caller = self.caller.account
#             elif utils.inherits_from(self.caller, "evennia.accounts.accounts.DefaultAccount"):
#                 # caller was already an Account
#                 self.character = self.caller.get_puppet(self.session)
#             else:
#                 self.character = None


from evennia import Command
# CHARGEN - Statistic Generation Commands:
class CmdSetStr(Command):
    """
    Set the STR of a character
    
    Usage:
      +str <1-40>
      
    This sets the strength of the current character. This can only be used during character generation.
    """
    key = "+str"
    help_category = "mush"
    
    def func(self):
        err_range = "You must supply a number between 1 and 40."
        err_high = "You don't have enough allocation points available. Try something lower."
        if not self.args:
            self.caller.msg(err_range)
            return
            try:
                power = int(self.args)
            except ValueError:
                self.caller.msg(err_range)
                return
            if not (1 <= power <= 40):
                self.caller.msg(err_range)
                return
            elif not (self.caller.db.junk >= power):
                self.caller.msg(err_high)
                return
            self.caller.db.stats['str'] = power
            self.caller.db.junk = int(self.caller.db.junk - power)
            self.caller.msg("Your Strength has become %i." % power)
            self.caller.msg("You have %i stat points left to allocate." % self.caller.db.junk)

class CmdSetDex(Command):
    """
    Set the DEX of a character
    
    Usage:
      +dex <1-40>
      
    This sets the dexterity of the current character. This can only be used during character generation.
    """
    key = "+dex"
    help_category = "mush"

    def func(self):
        err_range = "You must supply a number between 1 and 40."
        err_high = "You don't have enough allocation points available. Try something lower."
        if not self.args:
            self.caller.msg(err_range)
            return
        try:
            power = int(self.args)
        except ValueError:
            self.caller.msg(err_range)
            return
        if not (1 <= power <= 40):
            self.caller.msg(err_range)
            return
        elif not (self.caller.db.junk >= power):
            self.caller.msg(err_high)
            return
        self.caller.db.stats['dex'] = power
        self.caller.db.junk = int(self.caller.db.junk - power)
        self.caller.msg("Your Dexterity has become %i." % power)
        self.caller.msg("You have %i stat points left to allocate." % self.caller.db.junk)

class CmdSetRef(Command):
    """
    Set the REF of a character
    
    Usage:
      +ref <1-40>
      
    This sets the reflexes of the current character. This can only be used during character generation.
    """
    key = "+ref"
    help_category = "mush"
    
    def func(self):
        err_range = "You must supply a number between 1 and 40."
        err_high = "You don't have enough allocation points available. Try something lower."
        if not self.args:
            self.caller.msg(err_range)
            return
        try:
            power = int(self.args)
        except ValueError:
            self.caller.msg(err_range)
            return
        if not (1 <= power <= 40):
            self.caller.msg(err_range)
            return
        elif not (self.caller.db.junk >= power):
            self.caller.msg(err_high)
            return
        self.caller.db.stats['ref'] = power
        self.caller.db.junk = int(self.caller.db.junk - power)
        self.caller.msg("Your Reflexes have become %i." % power)
        self.caller.msg("You have %i stat points left to allocate." % self.caller.db.junk)

class CmdSetFor(Command):
    """
    Set the FOR of a character
    
    Usage:
      +for <1-40>
      
    This sets the fortitude of the current character. This can only be used during character generation.
    """
    key = "+for"
    help_category = "mush"
    
    def func(self):
        err_range = "You must supply a number between 1 and 40."
        err_high = "You don't have enough allocation points available. Try something lower."
        if not self.args:
            self.caller.msg(err_range)
            return
        try:
            power = int(self.args)
        except ValueError:
            self.caller.msg(err_range)
            return
        if not (1 <= power <= 40):
            self.caller.msg(err_range)
            return
        elif not (self.caller.db.junk >= power):
            self.caller.msg(err_high)
            return
        self.caller.db.stats['for'] = power
        self.caller.db.junk = int(self.caller.db.junk - power)
        self.caller.msg("Your Fortitude has become %i." % power)
        self.caller.msg("You have %i stat points left to allocate." % self.caller.db.junk)

class CmdSetCon(Command):
    """
    Set the CON of a character
    
    Usage:
      +con <1-40>
      
    This sets the constitution of the current character. This can only be used during character generation.
    """
    key = "+con"
    help_category = "mush"
    
    def func(self):
        err_range = "You must supply a number between 1 and 40."
        err_high = "You don't have enough allocation points available. Try something lower."
        if not self.args:
            self.caller.msg(err_range)
        return
        try:
            power = int(self.args)
        except ValueError:
            self.caller.msg(err_range)
            return
        if not (1 <= power <= 40):
            self.caller.msg(err_range)
            return
        elif not (self.caller.db.junk >= power):
            self.caller.msg(err_high)
            return
        self.caller.db.stats['con'] = power
        self.caller.db.junk = int(self.caller.db.junk - power)
        self.caller.msg("Your Constitution has become %i." % power)
        self.caller.msg("You have %i stat points left to allocate." % self.caller.db.junk)

class CmdSetDis(Command):
    """
    Set the DIS of a character
    
    Usage:
      +dis <1-40>
      
    This sets the discipline of the current character. This can only be used during character generation.
    """
    key = "+dis"
    help_category = "mush"
    
    def func(self):
        err_range = "You must supply a number between 1 and 40."
        err_high = "You don't have enough allocation points available. Try something lower."
        if not self.args:
            self.caller.msg(err_range)
            return
        try:
            power = int(self.args)
        except ValueError:
            self.caller.msg(err_range)
            return
        if not (1 <= power <= 40):
            self.caller.msg(err_range)
            return
        elif not (self.caller.db.junk >= power):
            self.caller.msg(err_high)
            return
        self.caller.db.stats['dis'] = power
        self.caller.db.junk = int(self.caller.db.junk - power)
        self.caller.msg("Your Discipline has become %i." % power)
        self.caller.msg("You have %i stat points left to allocate." % self.caller.db.junk)

class CmdSetInt(Command):
    """
    Set the Intelligence of a character
    
    Usage:
      +int <1-40>
      
    This sets the intelligence of the current character. This can only be used during character generation.
    """
    key = "+int"
    help_category = "mush"
    
    def func(self):
        err_range = "You must supply a number between 1 and 40."
        err_high = "You don't have enough allocation points available. Try something lower."
        if not self.args:
            self.caller.msg(err_range)
            return
        try:
            power = int(self.args)
        except ValueError:
            self.caller.msg(err_range)
            return
        if not (1 <= power <= 40):
            self.caller.msg(err_range)
            return
        elif not (self.caller.db.junk >= power):
            self.caller.msg(err_high)
            return
        self.caller.db.stats['int'] = power
        self.caller.db.junk = int(self.caller.db.junk - power)
        self.caller.msg("Your Intelligence has become %i." % power)
        self.caller.msg("You have %i stat points left to allocate." % self.caller.db.junk)

class CmdSetWis(Command):
    """
    Set the WIS of a character
    
    Usage:
      +wis <1-40>
      
    This sets the wisdom of the current character. This can only be used during character generation.
    """
    key = "+wis"
    help_category = "mush"
    
    def func(self):
        err_range = "You must supply a number between 1 and 40."
        err_high = "You don't have enough allocation points available. Try something lower."
        if not self.args:
            self.caller.msg(err_range)
            return
        try:
            power = int(self.args)
        except ValueError:
            self.caller.msg(err_range)
        return
        if not (1 <= power <= 40):
            self.caller.msg(err_range)
            return
        elif not (self.caller.db.junk >= power):
            self.caller.msg(err_high)
            return
        self.caller.db.stats['wis'] = power
        self.caller.db.junk = int(self.caller.db.junk - power)
        self.caller.msg("Your Wisdom has become %i." % power)
        self.caller.msg("You have %i stat points left to allocate." % self.caller.db.junk)

class CmdSetLuc(Command):
    """
    Set the Luc of a character
    
    Usage:
      +luc <1-40>
      
    This sets the luck of the current character. This can only be used during character generation.
    """
    key = "+luc"
    help_category = "mush"
    
    def func(self):
        err_range = "You must supply a number between 1 and 40."
        err_high = "You don't have enough allocation points available. Try something lower."
        if not self.args:
            self.caller.msg(err_range)
            return
        try:
            power = int(self.args)
        except ValueError:
            self.caller.msg(err_range)
            return
        if not (1 <= power <= 40):
            self.caller.msg(err_range)
            return
        elif not (self.caller.db.junk >= power):
            self.caller.msg(err_high)
            return
        self.caller.db.stats['luc'] = power
        self.caller.db.junk = int(self.caller.db.junk - power)
        self.caller.msg("Your Luck has become %i." % power)
        self.caller.msg("You have %i stat points left to allocate." % self.caller.db.junk)

class CmdSetSoc(Command):
    """
    Set the Soc of a character
    
    Usage:
      +soc <1-40>
      
    This sets the social of the current character. This can only be used during character generation.
    """
    key = "+soc"
    help_category = "mush"
    
    def func(self):
        err_range = "You must supply a number between 1 and 40."
        err_high = "You don't have enough allocation points available. Try something lower."
        if not self.args:
            self.caller.msg(err_range)
            return
        try:
            power = int(self.args)
        except ValueError:
            self.caller.msg(err_range)
            return
        if not (1 <= power <= 40):
            self.caller.msg(err_range)
            return
        elif not (self.caller.db.junk >= power):
            self.caller.msg(err_high)
            return
        self.caller.db.stats['soc'] = power
        self.caller.db.junk = int(self.caller.db.junk - power)
        self.caller.msg("Your Social has become %i." % power)
        self.caller.msg("You have %i stat points left to allocate." % self.caller.db.junk)

class CmdSetReset(Command):
    """
    Resets the statistics of a character.
    
    Usage:
      +reset
      
    This resets the stats of the current character. This can only be used during character generation.
    """
    key = "+reset"
    help_category = "mush"
    
    def func(self):
        self.caller.db.stats['str'] = 0
        self.caller.db.stats['dex'] = 0
        self.caller.db.stats['ref'] = 0
        self.caller.db.stats['for'] = 0
        self.caller.db.stats['con'] = 0
        self.caller.db.stats['dis'] = 0
        self.caller.db.stats['int'] = 0
        self.caller.db.stats['wis'] = 0
        self.caller.db.stats['luc'] = 0
        self.caller.db.stats['soc'] = 0
        self.caller.db.junk = 200
        self.caller.msg("Your stats have been reset.")
        self.caller.msg("You have %i stat points left to allocate." % self.caller.db.junk)




