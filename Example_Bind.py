from tkinter import *
root=Tk()
root.title("Click Button")
root.geometry("250x150")
root["bg"]="Violet"
ref_x=0
ref_y=0
btn=Button(root,text = "Click Me!" , font = ("Courier" , "8" , "bold") ,  bg = "Gold" , fg = "Green" , relief = RAISED , borderwidth = 3)
x=0
y=0
def down():
    global y
    y=y+10
    btn.place(y = ref_y+y)
def up():
    global y
    y=y-10
    btn.place(y = ref_y+y)
def right():
    global x
    x=x+10
    btn.place(x = ref_x+x)
def left():
    global x
    x=x-10
    btn.place(x = ref_x+x)
root.bind("<s>",lambda x:down())
root.bind("<d>",lambda x:right())
root.bind("<w>",lambda x:up())
root.bind("<a>",lambda x:left())
root.mainloop()