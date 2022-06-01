import game
import utils.common as common

def main():
    ans = game.ansNums()
    ev = game.checkNums(ans)
    print(f"bite {ev[0]} eat {ev[1]}")
    game.changeTurn()
    game.turn += 1

if __name__ == '__main__':
    game.init()
    game.start()
    while True:
        main()