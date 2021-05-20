import tkinter

x = 0
ani = 0


def animation():
    global ani
    ani = (ani + 1) % 4
    canvas.create_image(240, 300, image=img_dog[ani], tag="BG")
    root.after(50, animation)


def scroll_bg():
    global x
    x = x + 1
    if x == 480:
        x = 0
    canvas.delete("BG")
    canvas.create_image(x - 240, 150, image=img_bg, tag="BG")
    canvas.create_image(x + 240, 150, image=img_bg, tag="BG")
    root.after(50, scroll_bg)


root = tkinter.Tk()
canvas = tkinter.Canvas(width=480, height=320)
canvas.pack()
img_bg = tkinter.PhotoImage(file="park.png")
img_dog = [
    tkinter.PhotoImage(file="dog0.png"),
    tkinter.PhotoImage(file="dog1.png"),
    tkinter.PhotoImage(file="dog2.png"),
    tkinter.PhotoImage(file="dog3.png")
]

scroll_bg()
animation()
root.mainloop()
