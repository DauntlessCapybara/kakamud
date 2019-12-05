"""
GenCommands
Commands for Character Generation
"""
from evennia import default_cmds
from evennia import 

class CmdSetStat(Command):
    """
    Set the statistic of a character
    
    Usage:
      +stat str <1-40>
      
    This sets the strength of the current character. This can only be used during character generation.
    """
    key = "+stat"
    help_category = "mush"
    
    def func(self):
        err_range = "You must supply a number between 1 and 40."
        err_high = "You don't have enough allocation points available. Try something lower."
    err_stat = "You didn't specify a valid statistic to change. Check the stat's code and try again."
        if not self.args:
            self.caller.msg(err_range)
            return
        if not (self.args.split(" ")[0].strip) in self.caller.db.stats:
            self.caller.msg(err_stat)
            return
        stat = self.args.split(" ")[0].strip
        try:
            power = int(self.args.split(" ")[1])
        except ValueError:
            self.caller.msg(err_range)
            return
        if not (1 <= power <= 40):
            self.caller.msg(err_range)
            return
        elif not (self.caller.db.junk >= power):
            self.caller.msg(err_high)
            return
        self.caller.db.stats[stat] = power
        self.caller.db.junk = int(self.caller.db.junk - power)
        self.caller.msg(stat.upper + " has been set to %i." % power)
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