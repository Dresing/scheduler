from random import randint

class Schedule:

    def __init__(self):

        self.rooms = 13
        self.time = 13
        self.teams = 19
        self.setting = [[[] for x in range(self.rooms)] for y in range(self.time)]

        self.legal = True


    def assign(self, room, time, team):
        self.setting[room][time].append(team)

    def isOccupied(self, room, time):
        return True if len(self.setting[room][time]) > 1 else False

    def findFreeRoom(self, time):

        available = []

        for i in range(self.rooms):
            if(not self.isOccupied(i, time)):
                available.append(i)

        if len(available) == 0:
            return False

        return available[randint(0, len(available) - 1)]









s = Schedule()

for i in range(1000):

    for i in range(19):
        for j in range(13):
            room = s.findFreeRoom(j)
            if not room:
                print('not')
                continue

            s.assign(room, j, i)


    print('Found')
