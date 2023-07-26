# UTILITY
# Program to perform calculations to gather KPI's
# By: Alex O'Brien
import GrabData


class Calculate:
    def __init__(self):
        self.data = GrabData.grabData()

    def getData(self):
        return self.data

    def getMax(self, f):
        return self.data

    def getMin(self, field):
        return self.data

    def getPerLevel(self, field):
        return self.data

    def getByField(self):
        return self.data
