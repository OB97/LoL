# UTILITY
# Program to perform calculations to gather KPI's
# By: Alex O'Brien
import GrabData


class Calculate:
    def __init__(self):
        self.data = GrabData.grabData()

    ### GETTERS ###

    # get all data
    # @params: self
    # @return: {str:{str}}
    def getData(self):
        return self.data

    # get data by field name -
    ## info, partype, stats, tags
    # @params: self, field name
    # @return: [str,{str}]
    def getByField(self, f):
        fData = []
        for champ in self.data.keys():
            fData.append([champ, self.data[champ][f]])
        return fData

    ### OPERATIONS ###

    # find the highest value by stat name -
    ## armor, armorperlevel, attackdamage, attackdamageperlevel, attackrange, attackspeed, attackspeedperlevel, crit,
    ## critperlevel, hp, hpperlevel, hpregen, hpregenperlevel, movespeed, mp, mpperlevel, mpregen, mpregenperlevel,
    ## spellblock, spellblockperlevel
    # @params: self, stat name
    # @return: [str,{str}]
    def sMax(self, st):
        curMax = 0
        lstMax = []
        for lst in self.getByField("stats"):
            if int(lst[1][st]) > curMax:
                curMax = int(lst[1][st])
                lstMax = lst
        return lstMax

    # find the lowest value by stat name
    # @params: self, stat name
    # @return: [str,str]
    def sMin(self, st):
        curMin = 1000
        lstMin = []
        for lst in self.getByField("stats"):
            if int(lst[1][st]) < curMin:
                curMin = int(lst[1][st])
                lstMin = lst
        return lstMin

    # calculate a stat value at a specific level
    # @params: self, stat name
    # @return: [str,{str}]
    def sAtLevel(self, st, inLevel):
        return self.data
