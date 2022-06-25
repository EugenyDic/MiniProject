from tkinter import *

tk = Tk()
tk.title('Тыкалка')
tk.geometry("700x350")
n = 0


def nplus():
    global n
    n = n + 1
    label['text'] = str(n) + '$'

def nsbros():
    global n
    n = 0
    label['text'] = str(n) + '$'

btn1 = Button(text="Тык", background="#000", foreground="#fff",
padx="20", pady="8", font="16", command=nplus)
btn1.pack()

label = Label(tk, text=str(n)+'$', font=('Helvetica 30'))
label.pack()
btn2 = Button(text="Бум", background="#000", foreground="#fff",
padx="10", pady="4", font="8", command=nsbros)
btn2.pack()
mainloop()
