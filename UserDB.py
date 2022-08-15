# store users
# key, username, associated pool ids, default pool

class UserDB:
    def __init__(self, uzerz={1:["test", "test2"], 2:["test3", "test4"]}):
        self.list = uzerz

    def getUsers(self):
        return self.list

    def addUser(self, inp):
        self.list.append(inp)

