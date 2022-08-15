# stores users champ pool
# key, name, champs

class PoolDB:
    def __init__(self, pools={1:["a", 3, "b"], 2:["c",7, "d"], 3:["e",9 , "f"]}):
        self.pools = pools

    def getPools(self):
        return self.pools

    def addPool(self):
        pass