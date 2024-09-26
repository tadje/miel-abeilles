import random
FLOWERS = [(796, 310), (774, 130), (116, 69), (908, 534), (708, 99), (444, 428), (220, 307), (501, 287), (345, 560), (628, 311), (901, 639), (436, 619), (938, 646), (45, 549), (837, 787), (328, 489), (278, 434), (704, 995), (101, 482), (921, 964), (493, 970), (494, 898), (929, 389), (730, 742), (528, 794), (371, 429), (98, 711), (724, 631), (573, 903), (964, 726), (213, 639), (549, 329), (684, 273), (273, 105), (897, 324), (508, 31), (758, 405), (862, 361), (898, 898), (2, 897), (951, 209), (189, 739), (602, 68), (437, 601), (330, 410), (3, 517), (643, 404), (875, 407), (761, 772), (276, 666)]
POSITION_BEEHIVE = (500, 500)
class Bee:
    def __init__(self):
        self._id = "bee"
        self._path = random.sample(FLOWERS,len(FLOWERS) - 1)
        self._distance_path()
    def _distance_path(self):
        temp = POSITION_BEEHIVE 
        self._distance =  0
        for i in range(len(FLOWERS) - 1):
            self._distance += (self._path[i][0]-temp[0])**2 + (self._path[i][1] - temp[1])**2
            temp = self._path[i]
        self._distance += (temp[0] - 500)**2 +(temp[1] - 500)**2
        self._distance = self._distance**0.5

class Beehive:
    def __init__(self):
        self.bees = [Bee() for _ in range(100)]
bee = Bee()
print(bee._path)
print(bee._distance)
ruche = Beehive()
print(len(ruche.bees))