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
        self.cDB = cDB.ChampDB()
        self.uDB = uDB.UserDB()
        self.pDB = pDB.PoolDB()
        self.curUser = "0"
        self.selChamp = "0"

    # UI get all champs
    def giveChungus(self):
        x = input("Print all Champions or Search? (p or s)\n")
        if x == "p":
            print(list(self.cDB.getChamps().values()))
        elif x == "s":
            self.searchChump()

    # UI access pools
    def givePools(self):
        x = input("Print Pools or Add Pool? (p or a)\n")
        if x == "p":
            print(self.pDB.getPools())
        elif x == "a":
            z = input("Enter Pool Name: ")
            self.pDB.addPool(z + ",0")
            self.uDB.addUserPool(self.curUser, len(self.pDB.getPools()))
            self.givePools()

    # UI access users
    def giveUser(self):
        print(list(self.uDB.getUsers().values()))

    # UI search for champ
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
        # check if user exists
        for x in self.uDB.getUsers().items():
            if x[1][0] == self.curUser:
                p = True

        # if user exists
        if p:
            print("Welcome Back " + self.curUser + "!")
            print("**********\n")
            self.welcome()
        else:
            add = input("User Not Found! Add User? (y or n)\n")
            if add == "n":
                # restart sign in
                self.signIn()
            elif add == "y":
                # add user writes new user into users.txt
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
