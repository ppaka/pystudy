import random

def rolling_dice(pip):
    n = random.randint(1, pip)
    print(pip, "면 주사위 굴린 결과: ", n)

rolling_dice(12)
rolling_dice(6)
