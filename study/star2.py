def star(str, *num):
    l = len(num)
    for i in range(0, l):
        n = ""
        for j in range(0, num[i]):
            n = str + n
        print(n)


star("a", 1)
star("d", 1,2,3)