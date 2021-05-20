import datetime
import tkinter


def time_now():
    d = datetime.datetime.now()
    t = "{0} : {1} : {2}".format(d.hour, d.minute, d.second)
    label["text"] = t
    root.after(1000, time_now)


root = tkinter.Tk()
root.geometry("600x200")
fnt = ("NanumGothicRound", 60)
label = tkinter.Label(root, font=fnt)
label.pack()
time_now()
root.mainloop()
