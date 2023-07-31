# OBJECT
# Class to create and initialize champion objects
# By: Alex O'Brien

# noinspection SpellCheckingInspection
class Champion:

    def __init__(self, name, inData):
        self.name = name
        self.statData = inData
        for champ in self.statData:
            if champ[0] == self.name:
                self.armor = float(champ[1]["armor"])
                self.armorperlevel = float(champ[1]["armorperlevel"])
                self.ad = float(champ[1]["attackdamage"])
                self.adperlvl = float(champ[1]["attackdamageperlevel"])
                self.arange = float(champ[1]["attackrange"])
                self.aspeed = float(champ[1]["attackspeed"])
                self.aspeedperlvl = float(champ[1]["attackspeedperlevel"])
                self.crit = float(champ[1]["crit"])
                self.critperlvl = float(champ[1]["critperlevel"])
                self.hp = float(champ[1]["hp"])
                self.hpperlvl = float(champ[1]["hpperlevel"])
                self.hpregen = float(champ[1]["hpregen"])
                self.hpregenperlvl = float(champ[1]["hpregenperlevel"])
                self.movespeed = float(champ[1]["movespeed"])
                self.mp = float(champ[1]["mp"])
                self.mpperlvl = float(champ[1]["mpperlevel"])
                self.mpregen = float(champ[1]["mpregen"])
                self.mpregenperlvl = float(champ[1]["mpregenperlevel"])
                self.mr = float(champ[1]["spellblock"])
                self.mrperlvl = float(champ[1]["spellblockperlevel"])

    def statsAtLevel(self, lvl):
        newDict = {
            "Name": self.name,
            "Armor": round(self.getArmor() + self.getArmorPer() * lvl, 2),
            "Attack Damage": round(self.getAD() + self.getADPer() * lvl, 2),
            "Attack Range": round(self.getARange(), 2),
            "Attack Speed": "Todo",
            "Crit": round(self.getCrit() + self.getCritPer() * lvl, 2),
            "Health Points": round(self.getHP() + self.getHPPer() * lvl, 2),
            "Health Regen": round(self.getHPRegen() + self.getHPRegenPer() * lvl, 2),
            "Move Speed": round(self.getMoveSpeed(), 2),
            "Mana Points": round(self.getMP() + self.getMPPer() * lvl, 2),
            "Mana Regen": round(self.getMPRegen() + self.getMPRegenPer() * lvl, 2),
            "Magic Resist": round(self.getMR() + self.getMRPer() * lvl, 2)
        }
        return newDict

    def __repr__(self):
        return self.name

    def getArmor(self):
        return self.armor

    def getArmorPer(self):
        return self.armorperlevel

    def getAD(self):
        return self.ad

    def getADPer(self):
        return self.adperlvl

    def getARange(self):
        return self.arange

    def getASpeed(self):
        return self.aspeed

    def getASpeedPer(self):
        return self.aspeedperlvl

    def getCrit(self):
        return self.crit

    def getCritPer(self):
        return self.critperlvl

    def getHP(self):
        return self.hp

    def getHPPer(self):
        return self.hpperlvl

    def getHPRegen(self):
        return self.hpregen

    def getHPRegenPer(self):
        return self.hpregenperlvl

    def getMoveSpeed(self):
        return self.movespeed

    def getMP(self):
        return self.mp

    def getMPPer(self):
        return self.mpperlvl

    def getMPRegen(self):
        return self.mpregen

    def getMPRegenPer(self):
        return self.mpregenperlvl

    def getMR(self):
        return self.mr

    def getMRPer(self):
        return self.mrperlvl
