from . import user
import random
import utils.common as common

class Computer(user.User):
    def __init__(self):
        self.nums = []
        self.ansNums = []
        self.name = "computer"
        self.nowRespondent = False

    def createNum(self):
        tmp = []
        while len(tmp) < 3:
            num = random.randint(1, 9)
            if not num in tmp:
                tmp.append(num)
        return tmp
    
    def decideNum(self):
        self.nums = self.createNum()
        print(self.nums)