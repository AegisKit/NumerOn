from . import user
import utils.common as common

class Player(user.User):
    def __init__(self):
        self.nums = []
        self.ansNums = []
        self.name = "player"
        self.nowRespondent = False

    def createNum(self):
        tmp = []
        while True:
            for i in range(3):
                try:
                    tmp.append(int(input(f"{i+1}桁目の数字を入力 >> ")))
                except:
                    break

            if common.Common.checkNumForm(tmp):
                break
            else:
                print(f"値は重複なし整数で1桁ずつ入力してください")
                tmp = []
        return tmp
    
    def decideNum(self):
        self.nums = self.createNum()