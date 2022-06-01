from player import computer
from player import player
import utils.common as common
import sys

def init():
    global com
    global player

    isGame = False

    #コンピューター作成
    com = computer.Computer()
    #プレイヤー作成
    player = player.Player()

    com.decideNum()
    player.decideNum()
    print(f"Computer Number ***")
    print(f"Player Number ", end='')
    [print(i, end='') for i in player.nums]
    print("")


def start():
    global turn
    isGame = True
    turn = 1
    player.nowRespondent = True
    com.nowRespondent = False

def end(ans):
    if player.nowRespondent:
        print("============== Player WIN ===============")
        print(f"Ans ", end='')
        [print(i, end='') for i in ans]
        print("")
        print("Computer Number ", end='')
        [print(i, end='') for i in com.nums]
        print("")
        print(f"Turns {turn}")
        print("=========================================")
    else:
        print("============== Computer WIN =============")
        print(f"Ans ", end='')
        [print(i, end='') for i in ans]
        print("")
        print("Player Number ", end='')
        [print(i, end='') for i in player.nums]
        print("")
        print(f"Turns {turn}")
        print("=========================================")
    isGame = False

def ansNums():
    nums = []
    if player.nowRespondent:
        while 5:
            print("-------------Player Turn-------------------")
            for i in range(3):
                try:
                    nums.append(int(input(f"{i+1}桁目の数字を入力 >> ")))
                except:
                    break
            if common.Common.checkNumForm(nums):
                    break
            else:
                print(f"値は重複なし整数で1桁ずつ入力してください")
                nums = []
    else:
        print("-------------Computer Turn-----------------")
        nums = com.createNum()
    return nums


def checkNums(ans):
    bite = 0
    eat = 0

    #回答者判定
    if player.nowRespondent:
        nums = com.nums
    else:
        nums = player.nums
    
    for n, m  in zip(nums, ans):
        if n == m:
            eat += 1
        elif n in ans:
            bite += 1
        
    if eat == 3:
        end(ans)
        sys.exit()
    else:
        print(f"Ans ", end='')
        [print(i, end='') for i in nums]
        print("")
        return bite, eat

def changeTurn():
    if player.nowRespondent:
        player.nowRespondent = False
        com.nowRespondent = True
    else:
        player.nowRespondent = True
        com.nowRespondent = False