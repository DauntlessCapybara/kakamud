from evennia import DefaultCharacter

class Character(DefaultCharacter):
    def at_object_creation(self):
        self.db.junk = 0
        #level and experience
        self.db.level = 1
        self.db.exp = 0 
        #stats
        self.db.stats = {
                        'str':0, 
                        'dex':0, 
                        'ref':0, 
                        'for':0,
                        'con':0, 
                        'dis':0, 
                        'int':0, 
                        'wis':0, 
                        'luc':0, 
                        'soc':0
                        }

        #SKILLS PHYSICAL
        self.db.melee = 0
        self.db.ranged = 0
        self.db.shield = 0
        self.db.dodge = 0
        self.db.physical_fitness = 0
        self.db.amor = 0

        #SKILLS GENERAL/HYBRID
        self.db.perception = 0
        self.db.precision = 0
        self.db.trading = 0
        self.db.stealth = 0
        self.db.persuasion = 0
        self.db.firstaid = 0

        #SKILLS MAGIC
        self.db.magic_focus = 0
        self.db.relics = 0
        self.db.runes = 0
        self.db.spellpower = 0


        #consumable stats
        self.db.maxhp = int((self.db.stats['con']+self.db.stats['for'])/2+self.db.physical_fitness)
        self.db.hp = self.db.maxhp
        self.db.maxmana = int((self.db.stats['int']+self.db.stats['wis'])/2+self.db.magic_focus)
        self.db.mana = self.db.maxhp
        self.db.maxspirit = int((self.db.stats['soc']+self.db.stats['dis'])/20+int(self.db.level/5))
        self.db.spirit = self.db.maxspirit

        #traits that may or may not have mechanical impact
        self.db.gender = {'sub1':'It', 'sub2':'it', 'obj':'it', 'posdet':'its', 'pospred':'its', 
                        'self':'itself'}
        self.db.penis_size = "an average"
        self.db.height = "of average height"
        self.db.hair_length = "average length"
        self.db.hair_color = "brown"
        self.db.eye_color = "brown"


    # def look_describe(self):
    #   f"You see {name}. {self.db.gender['sub1']} is {self.db.height}."
    #   f"{self.db.gender['sub1']} has {self.db.hair_length} {self.db.hair_color} hair and {self.db.eye_color} eyes."
    #   f"{self.db.gender['sub1']} has {self.db.penis_size} penis."
    
    # def print_health(self):

    # def print_stats(self):

    # def print_skills(self):

    # def print_experience(self):
