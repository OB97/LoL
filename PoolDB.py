# stores users champ pool
# key, name, champs

class PoolDB:

    def getPools(self):
        final = {}
        i = 0
        pooltxt = open("pools.txt", "r")
        for line in pooltxt:
            a = line.split(",")
            name = a[0]
            z = a[1:]
            champs = list(map(int, z))
            final[i+1] = [name, champs]
            i = i + 1
        return final

    def addPool(self, inp):
        pooltxt = open("pools.txt", "a")
        pooltxt.writelines('\n' + inp)
