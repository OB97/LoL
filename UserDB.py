# key, name, associated pool ids, default pool

class UserDB:
    def __init__(self, uzerz={1:["alex", [1], 1], 2:["nate", [2, 3], 2]}):
        self.list = uzerz

    def getUsers(self):
        return self.list

    def addUser(self, inp):
        q = len(self.list) + 1
        self.list[q] = inp
