from tkinter import *
window= Tk()
window.config(width=500,height=400)
window.config(bg="black")
window.title("Km to Miles Converter")

inpuut = Entry()
inpuut.config(width=30)
inpuut.grid(row=0,column = 1)

lb1= Label()
lb1.config(text="Km",font=("Arial",20,"normal"),fg="white",bg="black")
lb1.grid(row=0,column=2)
lb2 = Label()
lb2.config(text="is converted into",font=("Arial",20,"normal"),fg="white",bg="black")
lb2.grid(row=1,column=0)

lb3 = Label()
val=0
lb3.config(text=f"{val}",font=("Arial",20,"bold"),fg="white",bg="black")
lb3.grid(row=1,column=1)

lb4 = Label()
lb4.config(text="Miles",font=("Arial",20,"normal"),fg="white",bg="black")
lb4.grid(row=1,column=2)

def when_clicked():
    num=float(inpuut.get())
    global val
    val=num/1.609
    lb3.config(text=f"{round(val,2)}",font=("Arial",20,"bold"),fg="white",bg="black")


butt= Button(text="calculate",command=when_clicked)
butt.grid(row=2,column=1)

window.mainloop()