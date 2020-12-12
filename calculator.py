from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget('text')
    print(text)
    if text=="=":
        value = 0
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(scvalue.get())
        scvalue.set(value)
        screen.update()
        
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("257x325")
root.title("Calculator")
root.configure(background="black")
root.wm_iconbitmap("icon.ico")
scvalue = StringVar()
scvalue.set("")

screen = Entry(root,textvar=scvalue, font="Times 25 bold", bg="gray10",fg="gray")
screen.pack(fill="x",padx=10,pady=10)

f = Frame(bg="black")

b = Button(f, text="7",font="Times 15 bold",padx=30, pady=8,bg="gray5",fg="white")
b.pack(fill="x",side=LEFT)
b.bind("<Button-1>",click)

b = Button(f, text="8",font="Times 15 bold",padx=30, pady=8,bg="gray5",fg="white")
b.pack(fill="x",side=LEFT)
b.bind("<Button-1>",click)

b = Button(f, text="9",font="Times 15 bold",padx=30, pady=8,bg="gray5",fg="white")
b.pack(fill="x",side=LEFT)
b.bind("<Button-1>",click)

f.pack(fill = "x",side=TOP)


f = Frame(bg="black")

b = Button(f, text="4",font="Times 15 bold",padx=30, pady=8,bg="gray5",fg="white")
b.pack(fill="x",side=LEFT)
b.bind("<Button-1>",click)

b = Button(f, text="5",font="Times 15 bold",padx=30, pady=8,bg="gray5",fg="white")
b.pack(fill="x",side=LEFT)
b.bind("<Button-1>",click)

b = Button(f, text="6",font="Times 15 bold",padx=30, pady=8,bg="gray5",fg="white")
b.pack(fill="x",side=LEFT)
b.bind("<Button-1>",click)

f.pack(fill = "x",side=TOP)

f = Frame(bg="black")

b = Button(f, text="1",font="Times 15 bold",padx=30, pady=8,bg="gray5",fg="white")
b.pack(fill="x",side=LEFT)
b.bind("<Button-1>",click)

b = Button(f, text="2",font="Times 15 bold",padx=30, pady=8,bg="gray5",fg="white")
b.pack(fill="x",side=LEFT)
b.bind("<Button-1>",click)

b = Button(f, text="3",font="Times 15 bold",padx=30, pady=8,bg="gray5",fg="white")
b.pack(fill="x",side=LEFT)
b.bind("<Button-1>",click)

f.pack(fill = "x",side=TOP)

f = Frame(bg="black")

b = Button(f, text="=",font="Times 15 bold",padx=30, pady=8,bg="gray10",fg="white")
b.pack(fill="x",side=LEFT)
b.bind("<Button-1>",click)

b = Button(f, text="0",font="Times 15 bold",padx=30, pady=8,bg="gray5",fg="white")
b.pack(fill="x",side=LEFT)
b.bind("<Button-1>",click)

b = Button(f, text="*",font="Times 15 bold",padx=30, pady=8,bg="gray10",fg="white")
b.pack(fill="x",side=LEFT)
b.bind("<Button-1>",click)

f.pack(fill = "x",side=TOP)

f = Frame(bg="black")

b = Button(f, text="C",font="Times 15 bold",padx=28, pady=8,bg="gray10",fg="white")
b.pack(fill="x",side=LEFT)
b.bind("<Button-1>",click)

b = Button(f, text="+",font="Times 15 bold",padx=30, pady=8,bg="gray10",fg="white")
b.pack(fill="x",side=LEFT)
b.bind("<Button-1>",click)

b = Button(f, text="-",font="Times 15 bold",padx=31, pady=8,bg="gray10",fg="white")
b.pack(fill="x",side=LEFT)
b.bind("<Button-1>",click)

f.pack(fill = "x",side=TOP)


root.mainloop()