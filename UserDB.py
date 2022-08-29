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
        usertxt.close()
        return final

    def addUser(self, inp):
        usertxt = open("users.txt", "a")
        usertxt.writelines("\n" + inp)
        usertxt.close()

    def addUserPool(self, user, inp):
        added = False
        usertxt = open("users.txt", "r+")
        d = usertxt.readlines()
        usertxt.seek(0)
        for line in d:
            splitted = line.split(",")
            if splitted[0] == user:
                splitted.insert(len(splitted)-1, inp)
                changes = line.replace(line, ",".join(str(x) for x in splitted))
                added = True
                usertxt.write(changes)
            else:
                usertxt.write(line)
        usertxt.truncate()
        usertxt.close()

        if added:
            print("Pool added to User: " + user)
        else:
            print("User not found!")

    def setDefaultPool(self, inp):
        pass
