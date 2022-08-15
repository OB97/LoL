# interface with users
# user creation, user search
# main menu: edit pool, champ select, settings
# edit pool: add and remove champs from pool, organize into positions, save by name, set default
# champ select: run through a champ select to narrow pool and record selection
# settings: basic settings, edit individual champ attributes

import Brain as b

class UI:

    def __init__(self, br=b.Brain()):
        self.chumps = br.giveChumps()
        self.pools = br.givePools()
        self.users = br.giveUsers()
        self.curUser = "None"


    # UI get champs
    def giveChungus(self):
        return self.chumps

    # UI get pools
    def givePools(self):
        return self.pools

    # UI get users
    def giveUsers(self):
        print("Current User: " + self.curUser)
        return self.users

    # UI search champs
    def searchChump(self):
        i = input("Enter Champion: ")
        z = ""

        for x in self.chumps.items():
            if x[1][0] == i:
                z = x
        if z != "":
            print(z[1])
        else:
            print("Champion Not Found!")

    # UI sign in to retrieve info
    def signIn(self):
        q = input("Enter LoL Username: ")
        for x in self.users.items():
            if x[1][0] == q:
                self.curUser = q

if __name__ == "__main__":
    print("Running UI...")
    UI().signIn()
    UI().giveUsers()
    UI().searchChump()
