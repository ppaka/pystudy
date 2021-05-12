# print("∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙")
import random
import os

clear = lambda : os.system('cls')

pPos = 1
cPos = 1
end = False

def startGame():
    global pPos
    global cPos
    global end

    pPos = 1
    cPos = 1
    end = False

def board():
    global pPos
    global cPos
    global end

    if pPos > 30:
        pPos = 30
    if cPos > 30:
        cPos = 30

    print("∙" * (pPos -1) + "P" + "∙" * (30 - pPos) + "Goal")
    print("∙" * (cPos -1) + "C" + "∙" * (30 - cPos) + "Goal")

    if pPos >= 30 and cPos >= 30:
        print("비겼습니다.")
        end = True
    elif pPos >= 30 and cPos < 30:
        print("당신의 승리.")
        end = True
    elif pPos < 30 and cPos >= 30:
        print("상대의 승리.")
        end = True


def roll():
    global pPos
    global cPos
    global end

    pRandom = random.randint(1, 6)
    print("\n주사위를 굴립니다: " + str(pRandom))
    pPos += pRandom

    input("[넘기려면 Enter키를 눌러주세요]")

    if pPos >= 30:
        return;

    cRandom = random.randint(1, 6)
    print("상대가 주사위를 굴립니다: " + str(cRandom))
    cPos += cRandom

    input("[결과를 확인하려면 Enter키를 눌러주세요]")

    if cPos >= 30:
        return;


startGame()

while end == False:
    clear()
    board()
    input("[주사위를 굴리려면 Enter키를 눌러주세요]")
    
    if end == False:
        roll()
        clear()
    else:
        break;