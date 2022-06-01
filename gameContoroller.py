import pygame
from pygame.locals import *
import sys
from player import player
from player import computer
import utils.common as common

START, SETTING, PLAY, RESULT = (0, 1, 2, 3)  # ゲーム状態

class gameContoroller():
    #コンストラクター
    def __init__(self):
        pygame.init()

        self.windowWidth = 700
        self.windowHeight = 600
        self.black = (0,0,0)
        self.gray = (230,230,250)
        self.gameState = START
        self.defFont = pygame.font.Font(None, 55)
        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self.startButton = None
        self.exitButton = None
   
        pygame.display.set_caption("NumerOn")
        self.screen.fill(self.gray)  

        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.draw()
            pygame.display.update()
            
            # イベント処理
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseClickEvent(event)
                
    
    def draw(self):
        self.screen.fill(self.gray) 
        if(self.gameState == START):
            print("START")
            titleFont = pygame.font.Font(None, 75)
            text = titleFont.render("NumerOn", True, self.black)   # 描画する文字列の設定
            text_rect = text.get_rect(center=(self.windowWidth//2, 100))
            self.screen.blit(text, text_rect)

            self.startButton = pygame.Rect(self.windowWidth//2-100, self.windowHeight//2-100, 200, 80)
            self.exitButton = pygame.Rect(self.windowWidth//2-100, self.windowHeight//2+50, 200, 80)
            startButtonText = self.defFont.render("START", True, self.black)
            exitButtonText = self.defFont.render("EXIT", True, self.black)

            pygame.draw.rect(self.screen, (0, 255, 0), self.startButton)
            pygame.draw.rect(self.screen, (255, 0, 0), self.exitButton)

            self.screen.blit(startButtonText, (self.windowWidth//2-63, self.windowHeight//2-78))
            self.screen.blit(exitButtonText, (self.windowWidth//2-50,self.windowHeight//2+73))
        elif(self.gameState == SETTING):
            print("SETTING")
            test = pygame.Rect(self.windowWidth//2-100, self.windowHeight//2-100, 200, 80)
            testText = self.defFont.render("1", True, self.black)
            pygame.draw.rect(self.screen, (0, 255, 0), test)
            self.screen.blit(testText, (self.windowWidth//2-63, self.windowHeight//2-78))

    def mouseClickEvent(self, event):
        # Start画面でのイベント処理
        if self.gameState == START:
            if self.startButton.collidepoint(event.pos) and (event.button == 1):
                self.gameState = SETTING
                print(f"gameState {self.gameState}")
            if self.exitButton.collidepoint(event.pos) and (event.button == 1):
                print("exit button was pressed")
                pygame.quit() 
                sys.exit()
        if self.gameState == SETTING:
            pass
        

    def start(self):
        global com
        global player
        global turn

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
        
        turn = 1
        player.nowRespondent = True
        com.nowRespondent = False

    def end(self, ans):
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

    def ansNums(self):
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


    def checkNums(self, ans):
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