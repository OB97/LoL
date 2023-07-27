# UTILITY
# Program to perform calculations on champion objects to gather KPI's
# By: Alex O'Brien
import GrabData


class Calculate:
    def __init__(self, objList):
        self.data = objList

    def statsAtLevel(self, name, lvl):
        curObj = self.data[name]
        newDict = {
            "Name": name,
            "Armor": round(curObj.getArmor() + curObj.getArmorPer() * lvl, 2),
            "Attack Damage": round(curObj.getAD() + curObj.getADPer() * lvl, 2),
            "Attack Range": round(curObj.getARange(), 2),
            "Attack Speed": "Todo",
            "Crit": round(curObj.getCrit() + curObj.getCritPer() * lvl, 2),
            "Health Points": round(curObj.getHP() + curObj.getHPPer() * lvl, 2),
            "Health Regen": round(curObj.getHPRegen() + curObj.getHPRegenPer() * lvl, 2),
            "Move Speed": round(curObj.getMoveSpeed(), 2),
            "Mana Points": round(curObj.getMP() + curObj.getMPPer() * lvl, 2),
            "Mana Regen": round(curObj.getMPRegen() + curObj.getMPRegenPer() * lvl, 2),
            "Magic Resist": round(curObj.getMR() + curObj.getMRPer() * lvl, 2)
        }
        return newDict
