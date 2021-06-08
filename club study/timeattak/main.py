import datetime
import random

AL = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
r = ''
start_time = ''


def start():
    global start_time
    start_time = datetime.datetime.now()
    choice()
    game()


def choice():
    global r
    r = random.choice(AL)
    al = ""
    for i in AL:
        if r != i:
            al = al + i

    print(al)


def game():
    inp = input('[사라진 알파벳은?]\n')
    end_time = datetime.datetime.now()
    time = (end_time - start_time).seconds
    if inp == r:
        print(time, '초 걸림')
        print('맞음')
    else:
        print('틀림, 다시시도')
        game()


while True:
    start()
