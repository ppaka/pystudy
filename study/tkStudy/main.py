import tkinter

p = 0

def main_proc():
    global p
    p += 20
    labell.place(x=p, y=180)
    base.after(1000, main_proc)

def btn_click():
    button["text"] = "클릭했다"

base = tkinter.Tk()
base.title("첫번째 윈도우")
base.geometry("640x360")

label = tkinter.Label(base, text="문자열", font=("System", 30))
label.place(x=0, y=0)
labell = tkinter.Label(base, text="플레이어", font=("System", 20))

button = tkinter.Button(base, text="클릭")
button.place(x=580, y=310)
labell.place(x=0, y=0)
main_proc()

base.mainloop()
