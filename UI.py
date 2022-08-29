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

    def __init__(self, cDB=ChampDB, pDB=PoolDB, uDB=UserDB):
        self.uDB = uDB.UserDB()
        self.pDB = pDB.PoolDB()
        self.chumps = cDB.ChampDB().getChamps()
        self.pools = pDB.PoolDB().getPools()
        self.users = uDB.UserDB().getUsers()
        self.curUser = "None"
        self.selChamp = "None"

    # UI get all champs
    def giveChungus(self):
        print(list(self.chumps.values()))

    # UI get current user's pools
    def givePools(self):
        # get input
        z = input("Print pools or Add pool? (p or a)\n")
        # if user wants to print pools
        if z == "p":
            # update self.pools in case of addition
            self.pools = self.pDB.getPools()
            j = []
            k = []
            # iterate through users and grab pools held in current user
            for x in self.users.items():
                if x[1][0] == self.curUser:
                    j.append(x[1][1])
            # iterate through pools held by current user (j), iterate through all pools (y) grabbing matching pool ids
            for num in j[0]:
                for y in self.pools.items():
                    if y[0] == num:
                        k.append(y[1])
            print(k)
            print("**********")

        # if user adds a pool
        elif z == "a":
            m = input("Enter Pool Name: ")
            st = m + ",0"
            # add pool to pools.txt
            self.pDB.addPool(st)
            # add pool id to user.txt
            self.uDB.addUserPool(self.curUser, len(self.pools.items()))
            print("Pool " + m + " Added!")
            print("**********\n")
            self.givePools()

    # UI get saved users
    def giveUser(self):
        self.users = self.uDB.getUsers()
        print(list(self.users.values()))

    # UI search for champ
    def searchChump(self):
        print("\n**********")
        d = input("Enter Champion: ")
        i = d.lower()
        z = ""
        for x in self.chumps.items():
            if x[1][0] == i:
                z = x
        if z != "":
            print(z[1])
            print("**********")
            self.selChamp = z[1]
            self.welcome()
        else:
            print("Champion Not Found!")
            print("**********\n")
            self.searchChump()

    # UI sign in to retrieve info, set current user
    def signIn(self):
        print("\n**********")
        q = input("Enter Name: ")
        p = False
        self.curUser = q
        for x in self.users.items():
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
        d = input("Champions, Search, Users, Pools, Sign Out, or End?\n")
        i = d.lower()
        if i == "champions":
            print("**********")
            print("Current Selected Champ: " + self.selChamp[0])
            self.giveChungus()
        elif i == "search":
            print("**********")
            self.searchChump()
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
