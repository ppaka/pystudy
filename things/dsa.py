import random


def div_name(name):
    return name[0], name[1:]

# print(div_name("ㄹㅇㄴㅁ"))


def dice_list(num, repeat):
    result = []
    for r in range(1, repeat + 1):
        n = random.randint(1, num)
        result.append(n)
    return result


print(dice_list(6, 5))