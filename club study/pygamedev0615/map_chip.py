import tkinter


def mouse_click(e):
    px = e.x
    py = e.y
    print("마우스 포인터 좌표 : ({}, {})".format(px, py))
    mx = int(px / 48)
    my = int(py / 48)
    if 0 <= mx and mx <= 6 and 0 <= my and my <= 4:
        n = map_data[my][mx]
        print("여기 있는 맵 칩은" + CHIP_NAME[n])


CHIP_NAME = ["잔디", "꽃", "나무", "물"]

root = tkinter.Tk()
root.title("맵 데이터")
canvas = tkinter.Canvas(width=336, height=240)
canvas.bind("<Button>", mouse_click)
canvas.pack()

img = [
    tkinter.PhotoImage(
        file="D:\MyFolder\Projects\Python\pystudy\club study\pygamedev0615\chip0.png"),
    tkinter.PhotoImage(
        file="D:\MyFolder\Projects\Python\pystudy\club study\pygamedev0615\chip1.png"),
    tkinter.PhotoImage(
        file="D:\MyFolder\Projects\Python\pystudy\club study\pygamedev0615\chip2.png"),
    tkinter.PhotoImage(
        file="D:\MyFolder\Projects\Python\pystudy\club study\pygamedev0615\chip3.png")
]
# map_data = [
#     [0, 1, 0, 2, 2, 2, 2],
#     [3, 0, 0, 0, 2, 2, 2],
#     [3, 0, 0, 1, 0, 0, 0],
#     [3, 3, 0, 0, 0, 0, 1],
#     [3, 3, 3, 3, 0, 0, 0]
# ]
map_data = [
    [0, 1, 1, 1, 1, 2, 3],
    [0, 1, 3, 3, 1, 2, 3],
    [0, 1, 3, 3, 1, 2, 3],
    [0, 1, 3, 3, 1, 2, 3],
    [0, 1, 1, 1, 1, 2, 3]
]

for y in range(5):
    for x in range(7):
        n = map_data[y][x]
        canvas.create_image(x*48+24, y*48 + 24, image=img[n])
root.mainloop()
