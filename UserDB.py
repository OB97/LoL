# store users
# key, name, associated pool ids, default pool

class UserDB:

    def getUsers(self):
        final = {}
        i = 0
        usertxt = open("users.txt", "r")
        for line in usertxt:
            splitted = line.split(",")
            pools = splitted[1:len(splitted)-1]
            fin = list(map(int, pools))
            default = splitted[len(splitted)-1].rstrip()
            final[i+1] = [splitted[0], fin, int(default)]
            i = i+1
        return final

    def addUser(self, inp):
        usertxt = open("users.txt", "a")
        usertxt.writelines("\n" + inp)
