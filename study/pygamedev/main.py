import tkinter


def key_down(ctx):
    key_code = ctx.keycode
    label1["text"] = "KeyCode :" + str(key_code)
    key_sym = ctx.keysym
    label2["text"] = "KeySymbol :" + str(key_sym)


root = tkinter.Tk()
root.title("Game Window")
root.geometry("400x200")
root.bind("<ButtonPress>", key_down)
fnt = ("Arial", 30)
label1 = tkinter.Label(root, text="keycode", font=fnt)
label1.place(x=0, y=0)
label2 = tkinter.Label(root, text="keysym", font=fnt)
label2.place(x=0, y=100)
root.mainloop()
