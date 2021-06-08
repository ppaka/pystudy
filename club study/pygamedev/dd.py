import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas(width=480, height=320)
canvas.pack()
img_bg = tkinter.PhotoImage(file="park.png")
canvas.create_image(240, 150, image=img_bg)
root.mainloop()
