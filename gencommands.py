"""
GenCommands

Commands for Character Generation

"""
from evennia import default_cmds
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




