chino = 1
tippy = 1
import random
import datetime


def board():
    print("~" * (chino - 1) + "C" + "~" * (40 - chino) + "망한 커피")
    print("~" * (tippy - 1) + "T" + "~" * (40 - tippy) + "망한 커피")


board()


def chinogame():
    AL = ["a", "b", "c", "d", "e", "f", "g", ]

    r = random.choice(AL)
    al = ""
    for i in AL:
        if r != i:
            al = al + i

    print(al)
    start_time = datetime.datetime.now()
    print("치노 차례")
    print("사라진 알파벳은?")
    ans = input()
    if ans == r:
        print("카페라떼 카페모카 카푸치노!")
        end_time = datetime.datetime.now()
        time = (end_time - start_time).seconds
        global chino
        chino = chino + int(time)
        print(str(time) + "초만에 했군.")
        board()
    else:
        print("틀렸다 애송이")
        CH()
        board()


def tippygame():
    AK = ["a", "b", "c", "d", "e", "f", "g", ]

    r = random.choice(AK)
    ak = ""
    for i in AK:
        if r != i:
            ak = ak + i
    print(ak)
    start_time = datetime.datetime.now()
    print("티피 차례")
    print("사라진 알파벳은?")
    ans = input()
    if ans == r:
        print("카페라떼 카페모카 카푸치노!")
        end_time = datetime.datetime.now()
        time = (end_time - start_time).seconds
        global tippy
        tippy = tippy + int(time)
        print(str(time) + "초만에 했군.")
        board()
    else:
        print("틀렸다 애송이")
        TI()
        board()


def TI():
    global tippy
    tippy = tippy + 7
    if tippy > 40:
        tippy = 40


def CH():
    global chino
    chino = chino + 7
    if chino > 40:
        chino = 40


while True:
    chinogame()
    if (chino == 40):
        print("치노의 패배")
        break
    if (tippy == 40):
        print("티피의 패배")
        break
    tippygame()
    if (chino == 40):
        print("치노의 패배")
        break
    if (tippy == 40):
        print("티피의 패배")
        break
