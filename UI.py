# interface with users
# user creation, user search
# main menu: edit pool, champ select, settings
# edit pool: add and remove champs from pool, organize into positions, save by name, set default
# champ select: run through a champ select to narrow pool and record selection
# settings: basic settings, edit individual champ attributes

import ChampDB
import PoolDB
import UserDB


class UI:

    # initialize DBs, current user, and selected champ
    def __init__(self, cDB=ChampDB, pDB=PoolDB, uDB=UserDB):
        self.cDB = cDB.ChampDB()
        self.uDB = uDB.UserDB()
        self.pDB = pDB.PoolDB()
        self.curUser = "0"
        self.selChamp = "0"

    # UI access champs
    def giveChungus(self):
        x = input("Print all Champions or Search? (p or s)\n")
        if x == "p":
            print(list(self.cDB.getChamps().values()))
        elif x == "s":
            self.searchChump()

    # UI access pools
    def givePools(self):
        # get input
        z = input("Print pools or Add pool? (p or a)\n")

        # if user wants to print pools
        if z == "p":

            if self.pDB.getPools().items()[1][0] == "":
                print("No Pools Found!")
                self.givePools()

            # update self.pools in case of addition
            self.pDB.getPools()
            j = []
            k = []
            champlist = []
            z = []

            # iterate through users and grab pools held in current user
            for x in self.uDB.getUsers().items():
                if x[1][0] == self.curUser:
                    j.append(x[1][1])
            # iterate through pools held by current user (j), iterate through all pools (y) grabbing matching pool ids
            for num in j[0]:
                for y in self.pDB.getPools().items():
                    if y[0] == num:
                        k.append(y[1])
            # iterate through pools and champ list pulling champ names contained in pools
            for v in k:
                for f in self.cDB.getChamps().items():
                    if f[0] in v[1]:
                        champlist.append(f[1][0])
                z.append([v[0], champlist])
                champlist = []
            print(z)
            print("**********")

        # if user adds a pool
        elif z == "a":
            done = False
            m = input("Enter Pool Name: ")
            st = m
            while not done:
                n = input("Enter Champion: (end to stop)\n")
                if n != "end":
                    for val in self.cDB.getChamps().items():
                        if n == val[1][0]:
                            st = st + "," + str(val[0])
                elif n == "end":
                    done = True

            # add pool to pools.txt
            self.pDB.addPool(st)
            # add pool id to user.txt
            self.uDB.addUserPool(self.curUser, len(self.pDB.getPools().items()))
            print("Pool " + m + " Added!")
            print("**********\n")
            self.givePools()

    # UI get saved users
    def giveUser(self):
        self.uDB.getUsers()
        print(list(self.uDB.getUsers().values()))

    # UI search champs
    def searchChump(self):
        print("\n**********")
        d = input("Enter Champion: ")
        i = d.lower()
        z = ""
        for x in self.cDB.getChamps().items():
            if x[1][0] == i:
                z = x
        if z != "":
            print(z[1])
            print("**********")
            self.selChamp = z[1]
        else:
            print("Champion Not Found!")
            print("**********\n")
            self.searchChump()

    # UI sign, set current user
    def signIn(self):
        print("\n**********")
        q = input("Enter Name: ")
        p = False
        self.curUser = q
        for x in self.uDB.getUsers().items():
            if x[1][0] == self.curUser:
                p = True
        if p:
            print("Welcome Back " + self.curUser + "!")
            print("**********\n")
            self.welcome()
        else:
            add = input("User Not Found! Add User? (y or n)\n")
            if add == "n":
                self.signIn()
            elif add == "y":
                self.uDB.addUser(q + ",0" + ",0")
                print("User " + q + " Added!")
                print("**********\n")
                self.welcome()

    # UI main loop
    def welcome(self):
        print("\n**********")
        print("Current User: " + self.curUser)
        d = input("Champions, Users, Pools, Sign Out, or End?\n")
        i = d.lower()
        if i == "champions":
            print("**********")
            print("Current Selected Champ: " + self.selChamp[0])
            self.giveChungus()
        elif i == "users":
            print("**********")
            self.giveUser()
        elif i == "pools":
            print("**********")
            self.givePools()
        elif i == "sign out":
            print("**********")
            self.signIn()
        elif i == "end":
            exit()
        else:
            print("Invalid Input!")
            print("**********")

        self.welcome()


if __name__ == "__main__":
    print("Running UI...")
    UI().signIn()
