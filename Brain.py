# pulls data from database for organization and calculation based on user input
# get/set champ, pool, user
# champ attribute operations
# pool operations

import ChampDB as cDB
import PoolDB as pDB
import UserDB as uDB


class Brain:

    def __init__(self, champs=cDB.ChampDB(), pools=pDB.PoolDB(), userz=uDB.UserDB()):
        self.chumps = champs.getChamps()
        self.pools = pools.getPools()
        self.users = userz.getUsers()

    def giveChumps(self):
        return self.chumps
    def givePools(self):
        return self.pools
    def giveUsers(self):
        return self.users
