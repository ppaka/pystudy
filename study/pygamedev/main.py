import tkinter

root = tkinter.Tk()
root.title("Game Window")
root.geometry("400x200")

label = tkinter.Label(root, text="게임개발걸음마")
label.place(x=80, y=60)
root.mainloop()
