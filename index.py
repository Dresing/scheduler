from random import randint
from random import shuffle
from random import sample
class Schedule:

    def __init__(self):

        self.rooms = 13
        self.time = 13
        self.teams = 19
        self.setting = [[[] for x in range(self.rooms)] for y in range(self.time)]

        self.legal = True


    def assign(self, room, time, team):
        self.setting[room][time].append(team)

    def numFreeSlots(self, room, time):
        return 2 - len(self.setting[room][time])

    def numfreeSlotsAtRoom(self, room):

        count = 0

        for i in range(self.time):
            count += len(self.setting[room][i])


        return self.teams - count

    def findFreeRoom(self, time):

        two = []

        one = []

        for i in range(self.rooms):
            if(self.numFreeSlots(i, time) == 1):
                one.append(i)

            if(self.numFreeSlots(i, time) == 2):
                two.append(i)

        if self.numfreeSlotsAtRoom(i) == 0:
            return -1


        return 0
        #if(len(two) > 6):
            #return two[randint(0, len(two) - 1)]



    def __str__(self):
        s = [[str(e) for e in row] for row in self.setting]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        return str('\n'.join(table))





def reset():
    s = Schedule()

    teams = sample(range(19), len(range(19)))
    times = sample(range(13), len(range(13)))


    for i in teams:
        for j in times:
            room = s.findFreeRoom(j)

            if room == -1:
                return False
                print('happens')

            s.assign(room, j, i)

    return s



for i in range(10000):
    val = reset()

    if not val:
        continue

    print(val)
    exit()
