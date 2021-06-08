from tkinter import *
from tkinter import messagebox
import random
import datetime as t_game
import time
import tkinter

card = ["♣", "♠", "♥", "◆"]
p_h = 5
c_h = 5
ll = 0
count = 0
p_card = 0
good = 0
c_card = 0
la_start1 = None
la_start2 = None
la_ht1 = None
la_ht2 = None


def ttime():
    # card2 라는 함수를, 3000ms(3초) 뒤 실행
    start.after(3000, card2)


def card1():
    global ll
    global count
    global p_card
    global la_ht1
    global p_c
    global la_start1
    if la_ht1 is not None:
        la_ht1.destroy()
    la_ht1 = Label(start, text=(f"플레이어 체력: {p_h}"), font="궁서 30")
    la_ht1.place(x=0, y=500)
    if la_start1 is not None:
        la_start1.destroy()
    ll = random.randint(0, 3)
    p_card = random.randint(1, 5)
    la_start1 = Label(start, text=(f"{card[ll]}{p_card}"), font="궁서 80")
    la_start1.place(x=100, y=350)
    btn_card.destroy()
    ttime()


def card2():
    global ll, btn_card
    global count
    global c_card
    global la_start2
    global la_ht2
    global good
    if good == 0:
        if la_ht2 is not None:
            la_ht2.destroy()
        la_ht2 = Label(start, text=(f"컴퓨터 체력: {c_h}"), font="궁서 30")
        la_ht2.place(x=1220, y=500)
        if la_start2 is not None:
            la_start2.destroy()
        ll = random.randint(0, 3)
        c_card = random.randint(1, 5)
        la_start2 = Label(start, text=f"{card[ll]}{c_card}", font="궁서 80")
        la_start2.place(x=1270, y=350)
        btn_card = Button(start, text="카드내기", font="궁서 40", command=card1)
        btn_card.place(x=610, y=700)


btn_card = None


def start1():
    global start, btn_card
    global p_c
    global c_c
    des()
    start = Tk()
    start.title("할리갈리")
    start.geometry("1500x900")
    btn_card = Button(start, text="카드내기", font="궁서 40", command=card1)
    btn_card.place(x=610, y=700)
    btn_bell = Button(start, text="종", font="궁서 30")
    btn_bell.place(x=710, y=350)
    start.mainloop()


def rule1():
    rule = messagebox.showinfo(
        "설명서",
        "기본 할리갈리랑 룰이 같습니다.\n카드내기를 눌러 카드를 냅니다.\n그리고 컴퓨터가 카드를 냅니다.\n두 카드가 똑같은 모양이고\n숫자의 합이 5면 종을 칩니다.\n종을 잘못누르거나 컴퓨터가 먼저 종을 누르면 목숨이 1개씩 까입니다")


def des():
    main.destroy()


def main1():
    global main
    main = Tk()
    main.title("할리갈리")
    main.geometry("1500x900")
    main.resizable(False, False)
    la_main = Label(main, text="할리갈리", font="궁서 80")
    la_main.place(x=490, y=100)
    btn_start = Button(main, text="시작하기", font="궁서 40", command=start1)
    btn_start.place(x=190, y=620)
    btn_rule = Button(main, text=" 설명듣기", font="궁서 40", command=rule1)
    btn_rule.place(x=930, y=620)
    main.mainloop()


main1()
