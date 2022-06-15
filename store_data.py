class Champion:
    # constructor initializes stats, all passed in VIA champions.csv
    def __init__(self, name, title, attack, defense, magic, difficulty, group, x, y, w, h, tag1, tag2, partype, hp, hpperlevel, mp, mpperlevel, movespeed, armour, armourperlevel, spellblock, spellblockperlevel, attackrange, hpregen, hpregenperlevel, mpregen, mpregenperlevel, attackdamage, attackdamageperlevel, attackspeedperlevel, attackspeed):
        self.name = name
        self.title = title
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.difficulty = difficulty
        self.group = group
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.tag1 = tag1
        self.tag2 = tag2
        self.partype = partype
        self.hp = hp
        self.hpperlevel = hpperlevel
        self.mp = mp
        self.mpperlevel = mpperlevel
        self.movespeed = movespeed
        self.armour = armour
        self.armourperlevel = armourperlevel
        self.spellblock =- spellblock
        self.spellblockperlevel = spellblockperlevel
        self.attackrange = attackrange
        self.hpregen = hpregen
        self.hpregenperlevel = hpregenperlevel
        self.mpregen = mpregen
        self.mpregenperlevel = mpregenperlevel
        self.attackdamage = attackdamage
        self.attackdamageperlevel = attackdamageperlevel
        self.attackspeedperlevel = attackspeedperlevel
        self.attackspeed = attackspeed

    # getter methods
    def getDefense(self):
        return self.defense
    def getAttack(self):
        return self.attack
    def getName(self):
        return self.name
    def getTitle(self):
        return self.title
    def getMagic(self):
        return self.magic
    def getDifficulty(self):
        return self.difficulty
    def getGroup(self):
        return self.group
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getW(self):
        return self.w
    def getH(self):
        return self.h
    def getTags(self):
        return self.tag1 + self.tag2
    def getPartype(self):
        return self.partype
    def getHp(self):
        return self.hp
    def getHpLevel(self):
        return self.hpperlevel
    def getMp(self):
        return self.mp
    def getMpLevel(self):
        return self.mpperlevel

class Item:
    # constructor initializes data from items.csv
    def __init__(self, name, desc, cost, stat):
        self.name = name
        self.desc = desc
        self.cost = cost
        self.stat = stat